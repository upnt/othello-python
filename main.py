import os
from othello.othello import Othello


game = Othello()
os.system('cls')
game.draw()

for _ in range(60):
    text = Othello.input_index()
    if text is None:
        break

    row, column = text
    game.put(row, column)
    os.system('cls')
    game.draw()

print('Thank you for playing')
