import os
from othello.othello import Othello, Event


game = Othello()
num_space, num_black, num_white = game.count_point()

os.system('cls')
game.draw()
print('black ' + str(num_black) + ' / white ' + str(num_white))

while(True):
    text = Othello.input_index()
    if text is None:
        break

    row, column = text
    game.put(row, column)
    num_space, num_black, num_white = game.count_point()

    os.system('cls')

    game.draw()
    print('black ' + str(num_black) + ' / white ' + str(num_white))
    if game.event is Event.PASS:
        print('pass')
    elif game.event is Event.END:
        break

print()
print()
print()
if num_black > num_white:
    print('winner black')
    num_black += num_space
else:
    print('winner white')
    num_white += num_space

print('black ' + str(num_black) + ' / white ' + str(num_white))
print('Thank you for playing')
