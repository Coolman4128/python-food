import socket
import pickle
import commands1

class SocketConnection:
    address = ""
    port = ""
    conn = socket.socket()
    def setAddressPort(self, Address, Port):
        self.address = Address
        self.port = Port

    def getAddress(self):
        return self.address
    def getPort(self):
        return self.port

    def setConnection(self, Connection):
        self.conn = Connection

    def sendData(self, data):
        changedData = pickle.dump(data)
        self.conn.send(changedData)


def initsocket(HOST, PORT):
    server.bind((HOST,PORT))
    
def listenconn():
    server.listen()
    servertup = server.accept()
    conn.setConnection(servertup[0])
    conn.setAddressPort(servertup[1][0], servertup[1][1]) 


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conn = SocketConnection()

