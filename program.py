import numpy as np

class Board:
    def __init__(self,size = 7):
        print("Welcome to Connect 4! Please input the number of your move")
        self.size = size
        self.state = np.zeros((size, size), np.int16)
        self.print_board()

    def print_board(self):
        print()
        for x in range(0, self.size):
            for y in range(0, self.size):
                if self.state[x, y] == 1:
                    print(" x", end='')
                elif(self.state[x, y] == 2):
                    print(" y", end='')
                else:
                    print("  ", end='')
            print(" ")
        
        for x in range(0, self.size):
            print(" {}".format(x), end='')
        print()

board = Board()
