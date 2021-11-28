import socket

def initsocket(HOST, PORT):
    server.bind((HOST,PORT))
    
def listenconn():
    server.listen()
    servertup = server.accept()
    addrs = servertup[1]
    return addrs

def testsend(conn, addrs):
    with conn:
        print('Connected to', addrs)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(repr(data))
            conn.sendall(data)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



