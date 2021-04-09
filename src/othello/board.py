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


    def add(self, elm, x, y):
        self.__board[y][x] = elm


    def get(self, x, y):
        return self.__board[y][x]


    def __iter__(self):
        return iter(self.__board)


def draw(board):
    print(' ' * (len(str(board.height)) + 1), end='')
    draw_line(range(1, board.width + 1), expand=' ')

    print('-' * (len(str(board.height)) + 1), end='')
    draw_line('-' * board.width, expand='-')

    for i, line in enumerate(board):
        print(str(i + 1) + ' ', end='')
        draw_line(line, expand=' ')

        print('--', end='')
        draw_line('-' * board.width, expand='-')


def draw_line(line, expand=''):
    for elm in line:
        print('|', end='')
        print(expand, end='')
        if elm is None:
            print(' ', end='')
        else:
            print(elm, end='')
        print(expand, end='')

    print('|')
