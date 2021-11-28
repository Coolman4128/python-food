import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def initsocket(HOST, PORT):
    server.bind((HOST,PORT))
    
def listenconn():
    server.listen()
    return server.accept()

def testsend(conn, addrs):
    with conn:
        print('Connected to', addrs)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(repr(data))
            conn.sendall(data)


