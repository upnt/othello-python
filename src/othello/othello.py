from string import ascii_letters

from othello.board import RectBoard, draw, search_max_length
from othello.stone import Stone, Color, Candidate


class Othello:
    size = 8
    row_list = ascii_letters[26:26+size]
    column_list = list(map(str, range(1, size + 1)))

    def __init__(self, mode='game'):
        self.__board = RectBoard(Othello.size, Othello.size)
        self.__board.put(Stone(Color.WHITE), 3, 3)
        self.__board.put(Stone(Color.WHITE), 4, 4)
        self.__board.put(Stone(Color.BLACK), 3, 4)
        self.__board.put(Stone(Color.BLACK), 4, 3)

        self.__player_color = Color.BLACK
        self.__mode = mode

        if self.__mode == 'game':
            self.__put_candidate()


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
                        print(result)
                        break
        return result


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


    def next_turn(self):
        if self.__player_color is Color.BLACK:
            self.__player_color = Color.WHITE
        else:
            self.__player_color = Color.BLACK

        if not self.__put_candidate():
            if self.__player_color is Color.BLACK:
                self.__player_color = Color.WHITE
            else:
                self.__player_color = Color.BLACK
            return self.__put_candidate()

        return True

    def __put_candidate(self):
        self.__delete_candidate()
        candidate_list = self.__candidate_list()
        if len(candidate_list) == 0:
            return False
        for i, j in candidate_list:
            self.__board.put(Candidate(), i, j)
        return True

    def __delete_candidate(self):
        for i in range(Othello.size):
            for j in range(Othello.size):
                if isinstance(self.__board.get(i, j), Candidate):
                    self.__board.put(None, i, j)


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
