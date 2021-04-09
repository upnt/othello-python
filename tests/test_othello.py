from othello.othello import Othello

def test_gamemode():
    game_record = 'e6d6c3f3d7e7f8c8f7c7c5f5b8g8d8e8g4b4b5g5g6b6f6c6g7b7c4f4a8h8a7h7a6h6a5h5g2b2g3b3h3a3h4a4c2f2b1g1h2a2a1h1f1c1d1e1d2e2d3e3'
    game = Othello()
    for row, column in Othello.available_record(game_record):
        game.put(row, column)
    game.draw()


def test_testmode():
    game_record = 'e6d6c3f3d7e7f8c8f7c7c5f5b8g8d8e8g4b4b5g5g6b6f6c6g7b7c4f4a8h8a7h7a6h6a5h5g2b2g3b3h3a3h4a4c2f2b1g1h2a2a1h1f1c1d1e1d2e2d3e3'
    game = Othello()
    game.set_mode('test')
    for row, column in Othello.available_record(game_record):
        game.put(row, column)
    game.draw()
