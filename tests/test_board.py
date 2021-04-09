from othello.board import RectBoard


def test_board():
    width, height = 3, 4
    board = RectBoard(width, height)
    board.draw()

    test_patterns = []
    test_numbers = [1, 0, -1, 10**12]
    test_numbers.extend(range(width * height - len(test_numbers)))

    j = 0
    for i, test_number in enumerate(test_numbers):
        board.add(test_number, i % width, j)
        if i % width == 2:
            j += 1

    j = 0
    for i in range(width * height):
        assert board.get(i % width, j) == test_numbers[i]
        if i % width == 2:
            j += 1
