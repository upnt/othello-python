from string import ascii_letters

from othello.board import RectBoard, draw, search_max_length
from othello.stone import Stone, Color


class Othello:
    size = 8
    row_list = ascii_letters[26:26+size]
    column_list = list(map(str, range(1, size + 1)))

    def __init__(self):
        self.__board = RectBoard(Othello.size, Othello.size)
        self.__board.put(Stone(Color.WHITE), 3, 3)
        self.__board.put(Stone(Color.WHITE), 4, 4)
        self.__board.put(Stone(Color.BLACK), 3, 4)
        self.__board.put(Stone(Color.BLACK), 4, 3)

        self.__player_color = Color.BLACK
        self.__mode = 'game'

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


    def set_color(self, color):
        self.__player_color = color

    def set_mode(self, mode):
        self.__mode = mode

    def put(self, row, column):
        if self.__mode == 'game':
            self.game_put(row, column)
        elif self.__mode == 'test':
            self.test_put(row, column)

    def test_put(self, row, column):
        x = Othello.row_list.index(row)
        y = Othello.column_list.index(column)

        self.__board.put(Stone(self.__player_color), x, y)

    def game_put(self, row, column):
        x = Othello.row_list.index(row)
        y = Othello.column_list.index(column)

        if self.__board.get(x, y) is not None:
            return
        self.__board.put(Stone(self.__player_color), x, y)

        direction = [
                (-1, 0), (-1, 1), (0, 1), (1, 1), 
                (1, 0), (1, -1), (0, -1), (-1, -1)
            ]
        for x_i, y_i in direction:
            for i, j in self.__reverse_list(x, y, x_i, y_i):
                self.__board.get(i, j).reverse()

        if self.__player_color is Color.BLACK:
            self.__player_color = Color.WHITE
        else:
            self.__player_color = Color.BLACK


    def draw(self):
        return draw(self.__board, Othello.row_list, Othello.column_list, 1, True)

    def available_record(game_record):
        text = game_record.upper()
        return [text[i*2:(i+1)*2] for i in range(int(len(text) / 2))]

    def input_index():
        while(True):
            text = input()
            if text == 'exit':
                return None
            try:
                row, column = text.upper()
                if row in Othello.row_list and column in Othello.column_list:
                    return row, column
            except ValueError as e:
                print(e)

            print('please again')
