from othello.othello import Othello


def test_othello():
    game = Othello()
    game.put('F', '5')
    game.draw()
