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
        self.__board[x][y] = elm


    def get(self, x, y):
        return self.__board[x][y]


    def draw(self):
        print(' ' * (len(str(self.height)) + 1), end='')
        draw_line(range(1, self.width + 1), expand=' ')

        print('-' * (len(str(self.height)) + 1), end='')
        draw_line('-' * self.width, expand='-')

        for i, line in enumerate(self.__board):
            print(str(i + 1) + ' ', end='')
            draw_line(line, expand=' ')

            print('--', end='')
            draw_line('-' * self.width, expand='-')


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
