from othello.board import RectBoard, draw, search_max_length


def test_board():
    width, height = 3, 4
    board = RectBoard(width, height)

    test_patterns = []
    test_numbers = [1, 0, -1, 10**12]
    test_numbers.extend(range(width * height - len(test_numbers)))

    j = 0
    for i, test_number in enumerate(test_numbers):
        board.put(test_number, i % width, j)
        if i % width == 2:
            j += 1

    i = 0
    for line in board:
        for elm in line:
            assert elm == test_numbers[i]
            i += 1

    draw(board, map(str, range(board.width)), map(str, range(board.height)), search_max_length(board))
