import commands
import socketworks
import guiworks

socketworks.initsocket('192.168.1.108', 15000) #This code inits the socket, and will bind it to the specified
                                               #address and port.

guiworks.createwindow()

#Starts listening for connections, and when found it saves them to conn, and addrs
conn, addrs = socketworks.listenconn()    









