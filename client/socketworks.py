import socket

class clientSocket:
    clientS = None
    command = ""
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
                    self.command = self.clientS.recv(1024)
                except ConnectionResetError:
                    self.clientS.close()
                    break
                self.command = self.command.decode()




