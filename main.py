import os
from othello.othello import Othello, Event


def draw_othello(game):
    num_space, num_black, num_white = game.count_point()
    
    os.system('cls')
    game.draw()
    print('black ' + str(num_black) + ' / white ' + str(num_white))


def draw_result(game):
    num_space, num_black, num_white = game.count_point()
    if num_black > num_white:
        print('winner black')
        num_black += num_space
    else:
        print('winner white')
        num_white += num_space
    
    print('black ' + str(num_black) + ' / white ' + str(num_white))
    print('Thank you for playing')


if __name__ == '__main__':
    game = Othello()
    draw_othello(game)
    
    while(True):
        text = Othello.input_index()
        if text is None:
            break
    
        row, column = text
        game.put(row, column)
        draw_othello(game)
    
        if game.event is Event.PASS:
            print('pass')
        elif game.event is Event.END:
            break
    
    print()
    print()
    print()
    draw_result(game)
