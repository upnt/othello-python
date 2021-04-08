from stone import Stone, StoneState
from board import RectBoard


if __name__ == '__main__':
    board = RectBoard(8, 8)
    board.add(1, 3, 3)
    board.add(1, 4, 4)
    board.add(2, 4, 3)
    board.add(2, 3, 4)
    board.draw()
