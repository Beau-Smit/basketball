import pandas as pd
import numpy as np
import os
import yaml
from sim import Team

ROOT = r"C:\Users\bsmit\Desktop\Training\Basketball_simulation"

def load_all_teams():
    team_dict = {}
    with open(os.path.join(ROOT, "All_Teams.yaml"), 'r') as config:
        All_Teams = yaml.load(config)

    Pace_AllTeams = pd.read_excel(os.path.join(ROOT, "NBA_team_stats.xlsx"), sheet_name = "Pace")
    Scoring_AllTeams = pd.read_excel(os.path.join(ROOT, "NBA_team_stats.xlsx"), sheet_name = "Scoring")
    Shooting_AllTeams = pd.read_excel(os.path.join(ROOT, "NBA_team_stats.xlsx"), sheet_name = "Shooting_Breakdown")

    for team_1, team_2 in zip(All_Teams["Team_List_1"], All_Teams["Team_List_2"]):
        team_lookup_1, team_lookup_2 = team_1.replace("_", " "), team_2.replace("_", " ")
        row_idx_2 = Shooting_AllTeams["TEAM"] == team_lookup_2

        team_pace = Pace_AllTeams.loc[Pace_AllTeams["Team"] == team_lookup_1, "PossPerGame2018"].values

        team_ppp = Scoring_AllTeams.loc[Scoring_AllTeams["Team"] == team_lookup_1, "PPP2018"].values

        team_shot_bd = (Shooting_AllTeams.loc[row_idx_2, "%FGA2PT"].values[0], Shooting_AllTeams.loc[row_idx_2, "%FGA3PT"].values[0])

        made2 = Shooting_AllTeams.loc[row_idx_2, "FGM"] - Shooting_AllTeams.loc[row_idx_2, "3PM"]
        att2 = Shooting_AllTeams.loc[row_idx_2, "FGA"] - Shooting_AllTeams.loc[row_idx_2, "3PA"]
        pct2 = round((made2/att2)*100, 1)
        team_shot_bd_per = (pct2.values[0], Shooting_AllTeams.loc[row_idx_2, "3P%"].values[0])

        team_TO_rate = (Shooting_AllTeams.loc[row_idx_2, "TOV"].values[0]/team_pace)[0]

        team_dict[team_1] = Team(team_lookup_1, 0, 0, 0, *team_pace, *team_ppp, team_shot_bd, team_shot_bd_per, team_TO_rate)

    return team_dict
