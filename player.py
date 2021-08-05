from utils import console_input
from card import Card


class Player:
    def __init__(self, number: int, card: Card):
        self._number = number
        self._card = card
        self.lost = False

    @property
    def card(self) -> Card:
        return self._card

    @property
    def number(self) -> int:
        return self._number

    def __str__(self) -> str:
        return f"Игрок №{self.number}"

    def cross_keg_question(self, value) -> bool:
        raise NotImplementedError


class HumanPlayer(Player):
    def cross_keg_question(self, value) -> bool:
        return console_input(f"Зачеркнуть цифру {value}? (y/n)")


class ComputerPlayer(Player):
    def cross_keg_question(self, value) -> bool:
        if value in self._card:
            return True
        return False
