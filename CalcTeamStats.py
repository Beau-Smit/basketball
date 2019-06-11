from sim import Team
import pandas as pd
import numpy as np
import os

TEAMBANK = r"C:\Users\bsmit\Desktop\Training\DataBank\NBA\team_level"

teamnames = pd.read_csv(r"C:\Users\bsmit\Desktop\Training\Basketball_simulation\src\teamnames.csv")

Hsplits = pd.read_excel(r"C:\Users\bsmit\Desktop\Training\Basketball_simulation\src\SplitStats.xlsx", sheet_name = "Home")
Asplits = pd.read_excel(r"C:\Users\bsmit\Desktop\Training\Basketball_simulation\src\SplitStats.xlsx", sheet_name = "Away")

PerPoss = pd.read_pickle(r"C:\Users\bsmit\Desktop\Training\DataBank\NBA\team_level\serialized\StatsPer100Poss_current.pkl")
Pace = pd.read_pickle(r"C:\Users\bsmit\Desktop\Training\DataBank\NBA\team_level\serialized\AdvStats_2014-2019.pkl")
Pace = Pace.loc[Pace.Season == "18-19"]
print(Pace.head())
print(Pace.columns.values)

Hsplits["2PM"] = Hsplits["FGM"] - Hsplits["3PM"]
Hsplits["2PA"] = Hsplits["FGA"] - Hsplits["3PA"]
Hsplits["2P%"] = Hsplits["2PM"] / Hsplits["2PA"]
Asplits["2PM"] = Asplits["FGM"] - Asplits["3PM"]
Asplits["2PA"] = Asplits["FGA"] - Asplits["3PA"]
Asplits["2P%"] = Asplits["2PM"] / Asplits["2PA"]

splits = pd.merge(Hsplits, Asplits, on = "TEAM", suffixes = ("_H", "_A"))
df = pd.merge(teamnames, splits, left_on = "Full", right_on = "TEAM")
df2 = pd.merge(df, Pace, left_on = "Short", right_on = "TEAM", suffixes = ("", "_XX"))

# print(np.mean(df2.PF_H), np.std(df2.PF_H), np.mean(df2.PF_A))

def gather_stats():
    team_dict = {}
    for index, row in df2.iterrows():
        shot_bd_H = (round(row["2PA_H"], 3), round(row["3PA_H"], 3))
        shot_bd_A = (round(row["2PA_A"], 3), round(row["3PA_A"], 3))
        shot_bd_per_H = (round(row["2P%_H"], 3), round(row["3P%_H"]/100, 3), round(row["FT%_H"]/100, 3))
        shot_bd_per_A = (round(row["2P%_A"], 3), round(row["3P%_A"]/100, 3), round(row["FT%_A"]/100, 3))
        team_dict[row.Acronym] = Team(row.TEAM, 0, 0, 0, row.PACE, shot_bd_H, shot_bd_A, shot_bd_per_H, shot_bd_per_A, row.TOV_H, row.TOV_A)

    return team_dict

    # def __init__(self, team_name, points, wins, series_wins, pace, ppp, shot_bd_H, shot_bd_A, shot_bd_per_H, shot_bd_per_A, to_rate, *args, **kwargs)
    # Team(team_lookup_1, 0, 0, 0, *team_pace, *team_ppp, team_shot_bd, team_shot_bd_per, team_TO_rate)

gather_stats()