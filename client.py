import socket
from board import Board

HOST = "localhost"
PORT = 45651

class Client(): # connect on class init
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))
        print("Client - Connected")
    def send_move(self, move):
        self.sock.sendall(int.to_bytes(move))
    def recv_move(self):
        return int.from_bytes(self.sock.recv(256))
    def close(self):
        self.sock.close()

board = Board()
c = Client()
while True:
    print("Awaiting move from other player")
    move = c.recv_move()
    board.move(move) # invoke move() directly as the received move is valid
    if move == -1:
        break
    move = board.handle_move()
    c.send_move(move)
    if move == -1:
        break

c.close()
