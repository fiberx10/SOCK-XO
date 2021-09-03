#client
'''
    XO GAME
| X  | O  |  X |
| X  | X  |  O |
| X  | O  |  X |

PLAYER (x , y)>
'''

'''
############# PROTOCOLE #############
#>  #setup a new name
#?  #update
#$  #send data

'''
from os import system , name
import socket

class Connect(object) :
    def __init__(self , port  ,  host  ):
        self.port  = port
        self.host = host
        self.sock  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
    def setup(self  ,  name):
        data  = "#>" + name
        self.sock.sendall(data.encode())
    def send(self , msg):
        self.sock.sendall(msg.encode())
    def recieve(self , org):
        self.sock.sendall(org)
        data = self.sock.recv(1024)
        return data.decode("utf-8")

class Player(object) :
    def __init__(self , ):
        self.name  = input("your name  : ")
        if name  == 'nt' :
            _ = system('cls')
        else:
            _ = system('clear')

class Game(Player , Connect) :
     def __init__(self , port , host):
         super(Player).__init__()
         super(Connect).__init__(port , host)
         self.status = True
         self.run = True
         self.board = [[' ' , ' ' , ' '] , [' ' , ' ' , ' ' ] , [' ' , ' ' , ' '] ]
     def print(self):
         print("    XO GAME      ")
         for i in range(len(self.board)) :
             print("| " ,end="")
             for j in range(len(self.board[0])) :
                 print(self.board[i][j] ," | " , end="")
             print(" ")
     def start(self):
         print(self.name  , "> " ,  end="")
         x = input("")
         y = input("")
         return (x , y)
     def update(self , x , y , plr):
         for i in range(len(self.board)) :
             for j in range(len(self.board[0])) :
                 if (i == x and j == y) :
                     self.board[i][j] = plr
     def pause(self):
         self.status = False
     def trunoff(self):
         self.run = False
     def resume(self):
         self.status = True

if  __name__ == "__main__" :
    port  = 10000
    host  = '192.0.0.1'
    game  = Game(port  ,  host)

