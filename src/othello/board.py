class RectBoard:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__board = []
        for _ in range(self.__height):
            self.__board.append([None] * self.__width)

    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height


    def put(self, elm, x, y):
        self.__board[y][x] = elm


    def get(self, x, y):
        return self.__board[y][x]


    def __iter__(self):
        return iter(self.__board)


def draw(board, row, column, word_len, ismulti=False):
    if ismulti:
        word_len *= 2
    print(' ' * (len(str(board.height)) + 2), end='')
    _draw_line(row, expand=' ', word_len=word_len)

    print('-' * (len(str(board.height)) + 2), end='')
    _draw_line(['-' * (word_len + 2)] * board.width, word_len=word_len)

    for y, line in zip(column, board):
        if ismulti:
            word_len = int(word_len / 2)
        print(y.center(len(str(board.height)) + 2), end='')
        _draw_line(line, expand=' ', word_len=word_len, ismulti=ismulti)
        if ismulti:
            word_len *= 2

        print('-' * (len(str(board.height)) + 2), end='')
        _draw_line(['-' * (word_len + 2)] * board.width, word_len=word_len)


def _draw_line(line, word_len, expand='', ismulti=False):
    for elm in line:
        print('|', end='')
        print(expand, end='')
        if elm is None:
            if ismulti:
                print(' ' * word_len * 2, end='')
            else:
                print(' ' * word_len, end='')
        else:
            print(str(elm).rjust(word_len), end='')
        print(expand, end='')

    print('|')


def search_max_length(board):
    result = 0
    for line in board:
        for elm in line:
            if elm is None:
                continue
            if len(str(elm)) > result:
                result = len(str(elm))

    return result
