# X,Y,Z means rock, paper, scissors
rps_dict = {
    'X': {'points':1, 'A':3, 'B':0, 'C':6},
    'Y': {'points':2, 'A':6, 'B':3, 'C':0},
    'Z': {'points':3, 'A':0, 'B':6, 'C':3}    
}

# X,Y,Z means lose, draw, win
ldw_dict = {
    'X': {'A':3 , 'B':1, 'C':2 },
    'Y': {'A':4 , 'B':5, 'C':6 },
    'Z': {'A':8 , 'B':9, 'C':7 }
}


round1_points = 0
round2_points = 0
with open('input.txt') as f:
    lines = f.readlines()

# X,Y,Z means rock, paper, scissors
def round_one(game: list[str]):
    opp, me = game
    return rps_dict[me]['points'] + rps_dict[me][opp]

# X,Y,Z means lose, draw, win
def round_two(game: list[str]):
    opp, order = game
    return ldw_dict[order][opp]

games = [line.split() for line in lines] 
for game in games:
    round1_points += round_one(game)
    round2_points += round_two(game)

print(f'Round one with presumed strategy: {round1_points}') 
print(f'Round two with actual strategy: {round2_points}') 