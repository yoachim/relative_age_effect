import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO
from time import sleep


if __name__ == "__main__":

    root_str = 'https://www.hockey-reference.com/friv/birthyears.cgi?year='

    for year in range(1879, 2008):
        print(year)
        url = root_str + "%i" % year

        try:
            response = requests.get(url)
            response.raise_for_status()  # Check if the request was successful.

        except requests.exceptions.RequestException as e:
            print(f"Error fetching the webpage: {e}")

        # Get the commented out tables back
        # content = str(response.content).replace("<!--", "").replace("-->", "")

        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find_all("table")

        if len(table) > 0:
            df0 = pd.read_html(StringIO(str(table[0])))[0]
            
            df0.to_csv("hockey_dfs/%i_hockey.csv" % year)

        sleep(10)