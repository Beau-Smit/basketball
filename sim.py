import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

class Team:
    def __init__(self, team_name, points, wins, series_wins, pace, shot_bd_H, shot_bd_A, shot_bd_per_H, shot_bd_per_A, to_rate_H, to_rate_A, *args, **kwargs):
        self.team_name = team_name
        self.points = points
        self.wins = wins
        self.series_wins = series_wins
        self.pace = pace
        self.shot_bd_H = shot_bd_H
        self.shot_bd_A = shot_bd_A
        self.shot_bd_per_H = shot_bd_per_H
        self.shot_bd_per_A = shot_bd_per_A
        self.to_rate_H = to_rate_H
        self.to_rate_A = to_rate_A
        self.home = False
        
    def possession(self):
        if self.home:
            rate2, rate3 = self.shot_bd_H[0], self.shot_bd_H[1]
            make_rate_2, make_rate_3 = self.shot_bd_per_H[0], self.shot_bd_per_H[1]
            to_rate = self.to_rate_H
        else:
            rate2, rate3 = self.shot_bd_A[0], self.shot_bd_A[1]
            make_rate_2, make_rate_3 = self.shot_bd_per_A[0], self.shot_bd_per_A[1]
            to_rate = self.to_rate_A

        def shot(rate2, rate3, make_rate_2, make_rate_3):
            # 2 or 3?
            choice = np.random.binomial(n = 1, p = (rate3/100)) + 2
            # made shot?
            if choice == 2:
                make = np.random.binomial(n = 1, p = make_rate_2) # made shot = 1, miss = 0
            elif choice == 3:
                make = np.random.binomial(n = 1, p = make_rate_3) # made shot = 1, miss = 0
            else:
                raise ValueError("Shot choice was not 2 or 3.")
            return choice * make
        
        poss_result = np.random.binomial(n = 1, p = to_rate/100) # TO = 1, shot = 0
        if poss_result == 1:
            pts = 0
        else:
            pts = shot(rate2, rate3, make_rate_2, make_rate_3)
        
        self.points += round(pts, 0)
    
    def reset_game(self):
        self.home = False
        self.points = 0
    
    def make_home(self):
        self.home = True

    def reset_series(self):
        self.wins = 0

    def reset_series_wins(self):
        self.series_wins = 0

def get_poss_limit(Away, Home):
    A = np.random.normal(Away.pace, 4)
    B = np.random.normal(Home.pace, 4)
    avg_poss = np.mean([A, B])
    return int(avg_poss)

def New_game(Away, Home):
    # initialize game conditions
    Away.reset_game()
    Home.reset_game()
    Home.make_home()
    poss_count = 0
    poss_limit = get_poss_limit(Away, Home)
    while poss_count < poss_limit:
        Away.possession()
        Home.possession()
        poss_count += 1
    # print("Game Over. Results:\n" + str(Away.team_name) + " " + str(Away.points) + "\n" + str(Home.team_name) + " " + str(Home.points))
    if Away.points > Home.points:
        Away.wins += 1
    elif Home.points > Away.points:
        Home.wins += 1
    else:
        flip = np.random.randint(0, 2)
        if flip == 0:
            Away.wins += 1
        else:
            Home.wins += 1

def series(Away, Home, games):
    Away.reset_series()
    Home.reset_series()
    for i in range(games):
        New_game(Away, Home)
    # print("Series over:\n" + str(Away.team_name) + " " + str(Away.wins) + "\n" + str(Home.team_name) + " " + str(Home.wins))
    if Away.wins > Home.wins:
        Away.series_wins += 1
    else:
        Home.series_wins += 1

def MonteCarlo_sim(Away, Home, sims, series_length):
    Away.reset_series_wins()
    Home.reset_series_wins()
    for s in range(sims):
        series(Away, Home, series_length)
    print(Away.team_name + " series wins: " + str(Away.series_wins) + " " + Home.team_name + " series wins: " + str(Home.series_wins))

