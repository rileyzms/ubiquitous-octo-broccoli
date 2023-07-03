import socket
import time

HOST = "localhost"
PORT = 45651

class Client():
    def __init__(self): # connect on class init
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen()
        self.conn, addr = s.accept()
        print("Server - Connected by", addr)
    def send_move(self):
        time.sleep(1)
        self.conn.sendall(b'test')
    def recv_move(self):
        data = self.conn.recv(512)
        print("Received ", repr(data))
    def close(self):
        self.conn.close()

c = Client()
c.send_move()
c.recv_move()
c.close()
