from sim import *
from CalcTeamStats import gather_stats

SIMULATIONS = 10000
x, y = [], []

team_dict = gather_stats()

'''
'ATL', 'BKN', 'BOS', 'CHA', 'CHI', 'CLE', 
'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 
'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 
'NYK', 'OKC', 'ORL', 'PHI', 'PHX', 'POR', 
'SAC', 'SAS', 'TOR', 'UTA', 'WAS'
'''
Away = team_dict['BOS']
Home = team_dict['PHI']

for i in range(SIMULATIONS):
    New_game(Away, Home)
    x.append(i)
    y.append(Away.wins/(Away.wins + Home.wins))

print(Away.team_name + " win rate:")
print(Away.wins/(Away.wins + Home.wins))

plt.figure()
plt.scatter(x, y, s=1, c="green")
v = np.linspace(0, SIMULATIONS, 2)
plt.plot(v, (v*0)+0.5, '-r')
plt.title("Probability of " + Away.team_name + " defeating " + Home.team_name)

# fit the curve
# z = np.polyfit(x, y, 2)
# p = np.poly1d(z)
# plt.plot(x,p(x),"r--")

plt.show()