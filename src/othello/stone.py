from enum import Enum, auto


class Stone:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    def reverse(self):
        if self.__color == Color.BLACK:
            self.__color = Color.WHITE
            return

        if self.__color == Color.WHITE:
            self.__color = Color.BLACK
            return

    def __str__(self):
        if self.__color == Color.BLACK:
            return '○'

        if self.__color == Color.WHITE:
            return '●'

class Candidate:
    def __str__(self):
        return '・'

class Color(Enum):
    BLACK = auto()
    WHITE = auto()
