from enum import Enum, auto


class Stone:
    def __init__(self, state):
        self.state = state

    def reverse(self):
        if self.state == StoneState.BLACK:
            self.state = StoneState.WHITE
            return

        if self.state == StoneState.WHITE:
            self.state = StoneState.BLACK
            return

    def debug(self):
        if self.state == StoneState.BLACK:
            print('○')
            return

        if self.state == StoneState.WHITE:
            print('●')
            return

class StoneState(Enum):
    BLACK = auto()
    WHITE = auto()
