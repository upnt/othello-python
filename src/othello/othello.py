from string import ascii_letters

from othello.board import RectBoard, draw, search_max_length
from othello.stone import Stone, Color


class Othello:
    def __init__(self):
        self.__size = 8
        self.__board = RectBoard(self.__size, self.__size)
        self.__board.add(Stone(Color.WHITE), 3, 3)
        self.__board.add(Stone(Color.WHITE), 4, 4)
        self.__board.add(Stone(Color.BLACK), 3, 4)
        self.__board.add(Stone(Color.BLACK), 4, 3)

        self.__row = ascii_letters[26:26+self.__size]
        self.__column = range(1, self.__size + 1)

    def draw(self):
        return draw(self.__board, self.__row, self.__column, 1, True)
