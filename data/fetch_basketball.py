import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO
from time import sleep


if __name__ == "__main__":

    root_str = 'https://www.basketball-reference.com/friv/birthdays.fcgi?month='
    mid_str = "&day="

    for month in range(1, 13):
        for day in range(1, 32):
            print(month, day)
            url = "%s%i%s%i" % (root_str, month, mid_str, day) 

            try:
                response = requests.get(url)
                response.raise_for_status()  # Check if the request was successful.

            except requests.exceptions.RequestException as e:
                print(f"Error fetching the webpage: {e}")

            # Get the commented out tables back
            content = str(response.content).replace("<!--", "").replace("-->", "")

            soup = BeautifulSoup(content, "html.parser")
            table = soup.find_all("table")

            # nba/aba
            if len(table) > 0:
                df0 = pd.read_html(StringIO(str(table[0])))[0]
                df0.to_csv("basketball_dfs/%i_%i_nba.csv" % (month, day))
            # wnba
            if len(table) > 1:
                df1 = pd.read_html(StringIO(str(table[1])))[0]
                df1.to_csv("basketball_dfs/%i_%i_wnba.csv" % (month, day))

            sleep(10)