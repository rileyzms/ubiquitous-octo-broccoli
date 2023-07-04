import socket
from board import Board

HOST = "localhost"
PORT = 45651

class Server():
    def __init__(self): # connect on class init
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen()
        self.conn, addr = s.accept()
        print("Server - Connected by", addr)
    def send_move(self, move):
        self.conn.sendall(int.to_bytes(move))
    def recv_move(self):
        return int.from_bytes(self.conn.recv(256))
    def close(self):
        self.conn.close()

board = Board()
s = Server()
while True:
    move = board.handle_move()
    s.send_move(move)
    if move == -1:
        break
    print("Awaiting move from other player")
    move = s.recv_move()
    board.move(move) # invoke move() directly as the received move is valid
    if move == -1:
        break

s.close()
