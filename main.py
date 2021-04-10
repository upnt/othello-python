import os
from othello.othello import Othello, Event


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
    if game.event is Event.PASS:
        print('pass')
    elif game.event is Event.END:
        break

print('Thank you for playing')
