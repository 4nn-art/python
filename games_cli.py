import json
import fire



class GamesCLI:
    def __init__(self):
        self.file_name = 'games.json'
        with open(self.file_name, 'r') as file:
            self.games_data = json.load(file)

    def add(self, game_name, price):
        new_game = {'name': game_name, 'price': price}
        self.games_data['games'].append(new_game)
        self.save()
        print(new_game)

    def update(self, game_name, price):
        for game in self.games_data['games']:
            if game['name'] == game_name:
                game['price'] = price
                self.save()
                print(game)

    def remove(self, game_name):
        for game in self.games_data['games']:
            if game['name'] == game_name:
                self.games_data['games'].remove(game)
                self.save()
                return True
            
    def save(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.games_data, file, indent=4)


if __name__ == '__main__':
    fire.Fire(GamesCLI())