import socket
import threading
import pickle
import commands3

class clientSocket:
    clientS = None
    recData = None
    address = ""
    port = ""
    def __init__(self, address1, port1):
        self.address = address1
        self.port = port1
        self.clientS = socket.socket()
    def runLoop(self):
        while 1:
            self.clientS = socket.socket()
            try:
                self.clientS.connect((self.address,self.port))
                print("\nConnected to the server successfully\n")
            except:
                print("Failed to connect to server")
                continue  
            while 1:
                try:
                    self.recData = self.clientS.recv(1024)
                except ConnectionResetError:
                    self.clientS.close()
                    break
                self.recData = pickle.loads(self.recData)
                output = commands3.checkCommand(self.recData)
                self.clientS.send(output.encode())
                





