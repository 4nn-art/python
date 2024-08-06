import yaml
import json


with open('games.yml', 'r') as o_file:
    games_data = yaml.safe_load(o_file)

with open('games.json', 'w') as w_file:
    json.dump(games_data, w_file, indent=4)