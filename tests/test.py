from stone import Stone, Color
from board import RectBoard


def board_test():
    board = RectBoard(8, 8)
    board.add(Stone(Color.WHITE), 3, 3)
    board.add(Stone(Color.WHITE), 4, 4)
    board.add(Stone(Color.BLACK), 4, 3)
    board.add(Stone(Color.BLACK), 3, 4)

    board.get(3, 3).reverse()
    board.get(4, 3).reverse()
    board.draw()


if __name__ == '__main__':
    board_test()
