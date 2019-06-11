# Research Question: 
# Is offensive rebounding a tradeoff with transition defense?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

NBA_BANK = r"C:\Users\bsmit\Desktop\Training\DataBank\NBA"
PLAYER_DATA = os.path.join(NBA_BANK, "player_level", "serialized")
TEAM_DATA = os.path.join(NBA_BANK, "team_level", "serialized")

for f in os.listdir(TEAM_DATA):
    print(f)
    df = pd.read_pickle(os.path.join(TEAM_DATA, f))
    print(df.columns.values)


'''
BoxScore_2012-2018.pkl              teamAbbr
Divisions.pkl                       Team
PlayoffSeriesResults_1946-2011.pkl  tmIDWinner / tmIDLoser
Standings_2012-2018.pkl             teamAbbr
StatsByGame_2014-2018.pkl           Team / Opponent
StatsBySeason_1937-2011.pkl         tmID / name
StatsBySeason_1946-2016.pkl         Team
StatsPer100Poss_current.pkl         Team
'''
