
rps_dict = {
    'X': {'points':1, 'A':3, 'B':0, 'C':6},
    'Y': {'points':2, 'A':6, 'B':3, 'C':0},
    'Z': {'points':3, 'A':0, 'B':6, 'C':3}    
}

overall_points = 0
with open('input.txt') as f:
    lines = f.readlines()

games = [line.split() for line in lines] 
for game in games:
    opp, me = game
    overall_points += rps_dict[me]['points']
    overall_points += rps_dict[me][opp]

print(overall_points)   