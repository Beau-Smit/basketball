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

NBA_BANK = r"C:\Users\bsmit\Desktop\Training\DataBank\NBA"
PLAYER_DATA = os.path.join(NBA_BANK, "player_level", "serialized")
TEAM_DATA = os.path.join(NBA_BANK, "team_level", "serialized")
STATES = r"C:\Users\bsmit\Desktop\Training\DataBank\States\state_abbr.csv"

recent = pd.read_pickle(os.path.join(PLAYER_DATA, "Bio_1970-2016.pkl"))
alltime = pd.read_pickle(os.path.join(PLAYER_DATA, "Bio_Alltime.pkl"))

# combine 2 data sets based on name
recent.Player = recent.Player.str.replace("*", "")
alltime.Player = recent.Player.str.replace("*", "")
df = pd.merge(recent, alltime, how = 'inner', on = ["Player"])
df.Place_of_Birth = df.Place_of_Birth.str.strip()

pop = pd.read_csv(STATES)

# change from dictionary to dataframe
state_df = pd.DataFrame(df.groupby("Place_of_Birth")["Place_of_Birth"].count())
state_df['State'] = state_df.index.values

# merge state population data with state basketball info
demographic_df = pd.merge(state_df, pop, how = 'inner', on = 'State')

# exclude DC
demographic_df = demographic_df.loc[demographic_df.Abbr != 'DC']

demographic_df["RatePer100000"] = (demographic_df.Place_of_Birth/demographic_df.Population)*100000

scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
            [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]

data = [ dict(
        type='choropleth',
        colorscale = scl,
        autocolorscale = False,
        locations = demographic_df.Abbr,
        z = demographic_df.RatePer100000.astype(float),
        locationmode = 'USA-states',
        text = demographic_df.Place_of_Birth, # text in the hover
        marker = dict(
            line = dict (
                color = 'rgb(255,255,255)',
                width = 2
            ) ),
        colorbar = dict(
            title = "NBA Players per 100,000 people")
        ) ]

layout = dict(
        title = 'Where Are the Best Basketball Players From?',
        geo = dict(
            scope = 'usa',
            projection = dict( type='albers usa' ),
            showlakes = True,
            lakecolor = 'rgb(255, 255, 255)'),
             )
    
fig = dict(data = data, layout = layout)
py.iplot(fig, filename = 'd3-cloropleth-map', auto_open = True)


'''
same bday as me
print(df.loc[df["Birth Date"].str.startswith("April 25"), ])
print(df.College.value_counts())
print(df.Race.value_counts())
print(df.birth_city.value_counts())
print(df.loc[df["birth_state"] == "Minnesota", ])
print(df.loc[df.height > 220].sort_values(by = "height"))


if __name__ == "__main__":
    call a function here
'''