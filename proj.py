import yaml

with open('games.yml', 'r') as file:
    games_data = yaml.safe_load(file)
#print(games_data['games'][0]['price'])

# total_price = 0
# for game in games_data['games']:
#     price = game['price']
#     total_price = total_price + price
#print(total_price)

total_price = sum([game['price'] for game in games_data['games']])
print(total_price)
