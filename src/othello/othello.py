from string import ascii_letters

from othello.board import RectBoard, draw, search_max_length
from othello.stone import Stone, Color


class Othello:
    def __init__(self):
        self.__size = 8
        self.__board = RectBoard(self.__size, self.__size)
        self.__board.put(Stone(Color.WHITE), 3, 3)
        self.__board.put(Stone(Color.WHITE), 4, 4)
        self.__board.put(Stone(Color.BLACK), 3, 4)
        self.__board.put(Stone(Color.BLACK), 4, 3)

        self.__row = ascii_letters[26:26+self.__size]
        self.__column = list(map(str, range(1, self.__size + 1)))

        self.__player_color = Color.BLACK

    def __reverse_list(self, x, y, x_i, y_i):
        try:
            if self.__board.get(x + x_i, y + y_i) is None:
                return []

            if self.__board.get(x, y).color is self.__board.get(x + x_i, y + y_i).color:
                return []

            result = []
            i = x + x_i
            j = y + y_i
            while(True):
                result.append((i, j))
                i += x_i
                j += y_i
                if self.__board.get(i, j) is None:
                    return []

                if self.__board.get(x, y).color is self.__board.get(i, j).color:
                    return result


        except IndexError:
            return []


    def put(self, row, column):
        x = self.__row.index(row)
        y = self.__column.index(column)
        self.__board.put(Stone(self.__player_color), x, y)
        for i, j in self.__reverse_list(x, y, -1, 0):
            self.__board.get(i, j).reverse()

        if self.__player_color is Color.BLACK:
            self.player_color = Color.WHITE
        else:
            self.player_color = Color.BLACK


    def draw(self):
        return draw(self.__board, self.__row, self.__column, 1, True)
