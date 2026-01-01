import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO
from time import sleep


if __name__ == "__main__":

    root_str = 'https://www.baseball-reference.com/leagues/majors/'
    year = 1938
    tail_str = "-births.shtml"

    for year in range(1880, 2003):
        print(year)
        url = root_str + "%i" % year + tail_str

        try:
            response = requests.get(url)
            response.raise_for_status()  # Check if the request was successful.

        except requests.exceptions.RequestException as e:
            print(f"Error fetching the webpage: {e}")

        # Get the commented out tables back
        content = str(response.content).replace("<!--", "").replace("-->", "")

        soup = BeautifulSoup(content, "html.parser")
        table = soup.find_all("table")

        # Batting
        df0 = pd.read_html(StringIO(str(table[0])))[0]
        # Pitching
        df1 = pd.read_html(StringIO(str(table[1])))[0]
        
        df0.to_csv("baseball_dfs/%i_batting.csv" % year)
        df1.to_csv("baseball_dfs/%i_pitching.csv" % year)

        if len(table) > 2:
            df2 = pd.read_html(StringIO(str(table[2])))[0]
            df2.to_csv("baseball_dfs/%i_managers.csv" % year)

        sleep(10)