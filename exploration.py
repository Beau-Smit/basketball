# Research Question: 
# Is offensive rebounding a tradeoff with transition defense?

print('Started')
from time import process_time, asctime
start_time = process_time()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import plotly.plotly as py
import plotly.graph_objs as go
import datetime

NBA_BANK = r"C:\Users\bsmit\Desktop\Training\DataBank\NBA"
PLAYER_DATA = os.path.join(NBA_BANK, "player_level", "serialized")
TEAM_DATA = os.path.join(NBA_BANK, "team_level", "serialized")
STATES = r"C:\Users\bsmit\Desktop\Training\DataBank\States\state_abbr.csv"

# print(os.listdir(PLAYER_DATA))

# df = pd.read_pickle(os.path.join(PLAYER_DATA, "Combine_2009-2017.pkl"))
# print(df.sort_values('Body Fat'))
# df["ratio_arms"] = df["Wingspan"] / df["Height (No Shoes)"]
# print(df.sort_values("Height (No Shoes)", ascending = False)[["Player", "Height (No Shoes)", "Wingspan", "ratio_arms"]])

gamedata = pd.read_pickle(r"C:\Users\bsmit\Desktop\Training\DataBank\NBA\team_level\serialized\StatsByGame_2014-2018.pkl")

gamedata.Date = pd.to_datetime(gamedata.Date)
date_mask_1415 = (gamedata.Date >= datetime.datetime(2014, 10, 1)) & (gamedata.Date <= datetime.datetime(2015, 4, 30))
gamedata.loc[date_mask_1415, "Season"] = "14-15"

date_mask_1516 = (gamedata.Date >= datetime.datetime(2015, 10, 1)) & (gamedata.Date <= datetime.datetime(2016, 4, 30))
gamedata.loc[date_mask_1516, "Season"] = "15-16"

date_mask_1617 = (gamedata.Date >= datetime.datetime(2016, 10, 1)) & (gamedata.Date <= datetime.datetime(2017, 4, 30))
gamedata.loc[date_mask_1617, "Season"] = "16-17"

date_mask_1718 = (gamedata.Date >= datetime.datetime(2017, 10, 1)) & (gamedata.Date <= datetime.datetime(2018, 4, 30))
gamedata.loc[date_mask_1718, "Season"] = "17-18"

team_df = gamedata.loc[gamedata.Season == "17-18"].groupby("Team")
df = pd.DataFrame({"AvgPoints": team_df.TeamPoints.mean(), "SdPoints": team_df.TeamPoints.std()})#.transpose()
# print(df.sort_values("AvgPoints"))

# set seed
np.random.seed(23)
df["PTS"] = np.random.normal(df.AvgPoints, df.SdPoints)

print(df)

# for team in gamedata.Team.unique():
#     sub = gamedata.loc[gamedata.Team == team]
    # print(sub.Game == 1)


# print(np.mean(s))
# print(np.std(s))