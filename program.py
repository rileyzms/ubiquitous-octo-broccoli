import numpy as np

class Board:
    def __init__(self,size = 7):
        print("Welcome to Connect 4! Please input the number of your move")
        self.size = size
        self.state = np.zeros((size, size), np.int16)
        self.print_board()
        self.turn = 1

    def print_board(self):
        print()
        for x in range(0, self.size):
            for y in range(0, self.size):
                if self.state[x, y] == 1:
                    print(" X", end='')
                elif(self.state[x, y] == 2):
                    print(" O", end='')
                else:
                    print("  ", end='')
            print(" ")
        
        for x in range(self.size):
            print(" {}".format(x), end='')
        print()

    def move(self, pos):
        try:
            pos = int(pos)
        except (ValueError):
           print("Not a number")
           return False
        if(pos >= self.size or pos < 0):
            print("Please select move in range")
            return False

        for i in reversed(range(self.size)):
            if(self.state[i, pos] == 0):
                self.state[i, pos] = self.turn
                self.turn = 3 - self.turn #3-1=2, 3-2=1
                return True
        print("Row full")
        return False

board = Board()
while True:
    if board.move(input("Input move - ")):
        board.print_board()
