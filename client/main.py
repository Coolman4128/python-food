from socketworks import clientSocket
import socketworks
import commands

HOST = '192.168.1.178'
PORT = 15000

client = clientSocket(HOST,PORT)

client.runLoop()