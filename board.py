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
        for y in range(0, self.size):
            for x in range(0, self.size):
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

    def move(self, pos): # returns true if valid move
        try:
            pos = int(pos)
        except (ValueError):
            print("Not a number")
            return False
        if(pos >= self.size or pos < 0):
            print("Please select move in range")
            return False

        for i in reversed(range(self.size)):
            if(self.state[pos, i] == 0):
                self.state[pos, i] = self.turn
                self.turn = 3 - self.turn # 3-1=2, 3-2=1
                return True
        print("Row full")
        return False

    def check_win(self, x, y): # returns True in case of win, false otherwise
        down_diag, horizontal, up_diag, vert = 0, 0, 0, 0
        for i in [-3,-2,-1,1,2,3]: # Skipping 0, as we know that value is equal to the curr turn
            if x+i >= 0 and x+i < self.size:
                if self.state[x+i, y] == self.turn:
                    horizontal += 1
                    if horizontal >= 3:
                        return True
                else:
                    horizontal = 0
                if y-i >= 0 and y-i < self.size:
                    if self.state[x+i, y-i] == self.turn:
                        down_diag += 1
                        if down_diag >= 3:
                            return True
                    else:
                        down_diag = 0
                if y+i >= 0 and y+i < self.size:
                    if self.state[x+i, y+i] == self.turn:
                        up_diag += 1
                        if up_diag >= 3:
                            return True
                    else:
                        up_diag = 0
            if y+i >=0 and y+i < self.size:
                if self.state[x, y+i] == self.turn:
                    vert += 1
                    if vert >= 3:
                        return True
        return False
    def handle_move():
        i = input("Please input move - ")
        while !board.move(i):
            i = input("Invalid move, please input move - ")
        if check_win():
            return -1
        board.print_board()
        return i
