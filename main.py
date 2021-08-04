import random
import settings
from player import HumenPlayer, ComputerPlayer, Player
from card import Card
from utils import console_input, console_clear


class Game:

    def __init__(self):
        self.players: list[Player] = []
        self.kegs = []

    def generate_kegs(self):
        bag_range = range(settings.KEG_MIN_VAL, settings.KEG_MAX_VAL)
        self.kegs =  random.sample(bag_range, settings.KEG_MAX_VAL-1)    
    
    def choise_players(self):
        players_chosen = False
        while len(self.players) < 2 or not players_chosen:
            player_number = len(self.players) + 1
            card = Card()
            if console_input(f"Выберите {player_number}-го игрока: (y  - человек / n - компьютер)"):                
                player = HumenPlayer(player_number, card)                
            else:                
                player = ComputerPlayer(player_number, card)
            self.players.append(player)
            if player_number > 1:                 
                players_chosen = not console_input("Добавить еще одного игрока? (y/n)")        

    def print_round(self, player, keg_value, keg_index):
        console_clear()        
        keg_remaind = settings.KEG_MAX_VAL - keg_index
        print(f"Новый бочонок: {keg_value} (осталось {keg_remaind-1})")
        for p in self.players:
            print(f"--- Карточка игрока: {p} ---")
            if p.lost:                
                print("\n        Игрок выбыл\n")                
            else:                
                print(p.card)
            print("---------------------------------")
        print(f"Ход игрока: {player}")

    def run(self):
        self.choise_players()
        self.generate_kegs()
        
        win_player = None
        for i, keg_value in enumerate(self.kegs):            
            players_in_game = list(filter(lambda p: not p.lost, self.players))
            if len(players_in_game) == 1: 
                print(f"Игрок {players_in_game[0]} выйграл")
                break
            if win_player:
                print(f"Игрок {win_player} выйграл")
                break
            for player in players_in_game:                
                self.print_round(player, keg_value, i)
                cross_keg_answer = player.cross_keg_question(keg_value)
                if cross_keg_answer and keg_value in player.card:
                    player.card.cross_keg(keg_value)
                    if player.card.count_cros_keg == settings.COUNT_KEG * settings.COUNT_STR:
                        win_player = player
                        break
                elif not cross_keg_answer and keg_value not in player.card:
                    continue
                else:
                    player.lost = True                    

if __name__ == "__main__":
    game = Game()         
    game.run()
    
        
