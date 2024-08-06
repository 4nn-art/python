import yaml
import sys
import json

#print(sys.argv)
with open('games.yml', 'r') as file:
    games_data = yaml.safe_load(file)

# game_name = input("Hello, please enter the game to know a price: ")

for game in games_data['games']:
    if game['name'] == sys.argv[1]:
        #print(game['price'])
        #print(game)
        print(json.dumps(game, indent=4))
