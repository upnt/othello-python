from othello.stone import Stone, Color
from othello.board import RectBoard, draw

def test_overall():
    board = RectBoard(8, 8)

    board.add(Stone(Color.WHITE), 3, 3)
    board.add(Stone(Color.WHITE), 4, 4)
    board.add(Stone(Color.BLACK), 3, 4)
    board.add(Stone(Color.BLACK), 4, 3)

    draw(board)
