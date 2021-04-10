from string import ascii_letters
from enum import Enum, auto

from othello.board import RectBoard, draw, search_max_length
from othello.stone import Stone, Color, Candidate


class Event(Enum):
    PASS = auto()
    END = auto()


class Mode(Enum):
    GAME = auto()
    TEST = auto()


class Othello:
    size = 8
    row_list = ascii_letters[26:26+size]
    column_list = list(map(str, range(1, size + 1)))

    def __init__(self, mode=Mode.GAME):
        self.__board = RectBoard(Othello.size, Othello.size)
        self.__board.put(Stone(Color.WHITE), 3, 3)
        self.__board.put(Stone(Color.WHITE), 4, 4)
        self.__board.put(Stone(Color.BLACK), 3, 4)
        self.__board.put(Stone(Color.BLACK), 4, 3)

        self.__player_color = Color.BLACK
        self.__mode = mode
        self.__event = None

        if self.__mode is mode.GAME:
            self.__put_candidate()


    @property
    def event(self):
        return self.__event
    def __reverse_list(self, x, y, x_i, y_i):
        try:
            if not isinstance(self.__board.get(x + x_i, y + y_i), Stone):
                return []
            if self.__player_color is self.__board.get(x + x_i, y + y_i).color:
                return []

            result = []
            i = x + x_i
            j = y + y_i
            while(True):
                result.append((i, j))
                i += x_i
                j += y_i
                if not isinstance(self.__board.get(i, j), Stone):
                    return []

                if self.__player_color is self.__board.get(i, j).color:
                    return result


        except IndexError:
            return []


    def __candidate_list(self):
        result = []
        for w_i in range(Othello.size):
            for h_i in range(Othello.size):
                if self.__board.get(w_i, h_i) is not None:
                    continue
                direction = [
                        (-1, 0), (-1, 1), (0, 1), (1, 1), 
                        (1, 0), (1, -1), (0, -1), (-1, -1)
                    ]
                for x_i, y_i in direction:
                    if len(self.__reverse_list(w_i, h_i, x_i, y_i)) != 0:
                        result.append([w_i, h_i])
                        break
        return result


    def set_color(self, color):
        self.__player_color = color

    def set_mode(self, mode):
        self.__mode = mode

        if mode is Mode.GAME:
            self.__put_candidate()
        elif mode is Mode.TEST:
            self.__delete_candidate()

    def put(self, row, column):
        if self.__mode is Mode.GAME:
            self.__game_put(row, column)
        elif self.__mode == Mode.TEST:
            self.__test_put(row, column)

    def __test_put(self, row, column):
        x = Othello.row_list.index(row)
        y = Othello.column_list.index(column)

        self.__board.put(Stone(self.__player_color), x, y)

    def __game_put(self, row, column):
        x = Othello.row_list.index(row)
        y = Othello.column_list.index(column)

        if not isinstance(self.__board.get(x, y), Candidate):
            print(type(self.__board.get(x, y)))
            return
        self.__board.put(Stone(self.__player_color), x, y)

        direction = [
                (-1, 0), (-1, 1), (0, 1), (1, 1), 
                (1, 0), (1, -1), (0, -1), (-1, -1)
            ]
        for x_i, y_i in direction:
            for i, j in self.__reverse_list(x, y, x_i, y_i):
                self.__board.get(i, j).reverse()

        self.__next_turn()


    def __next_turn(self):
        self.__change_color()
        if not self.__put_candidate():
            self.__change_color()
            return self.__put_candidate()

        return True

    def __put_candidate(self):
        self.__delete_candidate()
        candidate_list = self.__candidate_list()
        if len(candidate_list) == 0:
            if self.__event is None:
                self.__event = Event.PASS
            else:
                self.__event = Event.END
            return False
        else:
            self.__event = None
        for i, j in candidate_list:
            self.__board.put(Candidate(), i, j)
        return True

    def __delete_candidate(self):
        for i in range(Othello.size):
            for j in range(Othello.size):
                if isinstance(self.__board.get(i, j), Candidate):
                    self.__board.put(None, i, j)

    def __change_color(self):
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
