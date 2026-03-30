import pandas as pd
import glob
import numpy as np


month_to_int = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
                "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
                "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12,
                "June": 6, "December": 12, "January": 1,
                "February": 2, "March": 3, "April": 4,
                "July": 7, "August": 8, "September": 9,
                "October": 10, "November": 11}


def consol_base():
    """Package up the baseball birthdays
    """
    files = glob.glob("baseball_dfs/*.csv")
    players = []
    managers = []

    keys = ["Name", "Birthdate", "Mgr"]

    for filename in files:

        temp_df = pd.read_csv(filename)

        year = filename.split("/")[1].split('_')[0]

        to_store = pd.DataFrame()
        for key in keys:
            try:
                to_store[key] = temp_df[key]
            except:
                pass
        to_store["year"] = int(year)

        to_store = to_store.dropna()

        month = [month_to_int[bd.split(" ")[0]] for bd in to_store["Birthdate"]]
        day = [int(bd.split(" ")[1]) for bd in to_store["Birthdate"]]

        to_store["month"] = month
        to_store["day"] = day

        if "mana" in filename:
            managers.append(to_store)
        else:
            players.append(to_store)

    players = pd.concat(players)
    managers = pd.concat(managers)

    # Drop NaNs
    players = players.dropna()
    managers = managers.dropna()

    # Drop duplicates
    players = players.drop_duplicates(["Name", "Birthdate"])

    players.to_csv("baseball_consolidated.csv")
    managers.to_csv("baseball_managers_consol.csv")


def consol_hock():
    files = glob.glob("hockey_dfs/*.csv")
    players = []
    keys = {"Player": "Name", "Birth Date": "Birthdate"}

    for filename in files:
        temp_df = pd.read_csv(filename, header=1)

        year = filename.split("/")[1].split('_')[0]
        to_store = pd.DataFrame()
        for key in keys:
            to_store[keys[key]] = temp_df[key]

        years = np.ones(to_store.shape[0])* int(year)

        bad = np.where(to_store["Birthdate"].values == "Birth Date")
        years[bad] = np.nan
        to_store["year"] = years

        to_store = to_store.dropna()

        month = [month_to_int[bd.split(" ")[0]] for bd in to_store["Birthdate"]]
        day = [int(bd.split(" ")[1]) for bd in to_store["Birthdate"]]

        to_store["month"] = month
        to_store["day"] = day

        players.append(to_store)

    players = pd.concat(players)
    players = players.dropna()
    players.to_csv("hockey_consolidated.csv")


def consol_bb(ss="nba"):
    files = glob.glob("basketball_dfs/*%s.csv" % ss)

    players = []
    keys = {"Player": "Name"}

    for filename in files:
        temp_df = pd.read_csv(filename, header=1)

        month = filename.split("/")[1].split('_')[0]
        day = filename.split("/")[1].split('_')[1]
        to_store = pd.DataFrame()
        for key in keys:
            to_store[keys[key]] = temp_df[key]
        to_store["month"] = int(month)
        to_store["day"] = int(day)
        year = np.zeros(temp_df.shape[0], dtype=int) + np.nan
        good = np.where(temp_df["Born"].values != "Born")[0]
        year[good] = temp_df["Born"].values[good]

        to_store["year"] = year


        players.append(to_store)

    players = pd.concat(players)
    players = players.dropna()
    players.to_csv("%s_consolidated.csv" % ss)


def consol_foot():
    files = glob.glob("football_dfs/*.csv")

    players = []
    keys = {"Player": "Name"}

    for filename in files:
        temp_df = pd.read_csv(filename, header=1)

        month = filename.split("/")[1].split('_')[0]
        day = filename.split("/")[1].split('_')[1]
        to_store = pd.DataFrame()
        for key in keys:
            to_store[keys[key]] = temp_df[key]
        to_store["month"] = int(month)
        to_store["day"] = int(day)
        year = np.zeros(temp_df.shape[0], dtype=int) + np.nan
        good = np.where(temp_df["Born"].values != "Born")[0]
        year[good] = temp_df["Born"].values[good]

        to_store["year"] = year


        players.append(to_store)

    players = pd.concat(players)
    players = players.dropna()
    players.to_csv("nfl_consolidated.csv")



if __name__ == "__main__":

    #consol_hock()
    #consol_base()
    #consol_bb(ss="nba")
    #consol_bb(ss="wnba")
    consol_foot()