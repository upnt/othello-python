from stone import Stone, Color
from board import RectBoard


def board_test():
    board = RectBoard(8, 8)
    board.add(1, 3, 3)
    board.add(1, 4, 4)
    board.add(2, 4, 3)
    board.add(2, 3, 4)
    board.draw()


if __name__ == '__main__':
    board_test()
