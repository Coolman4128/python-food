import commands
import socketworks
import guiworks



socketworks.initsocket('192.168.1.178', 15000) #Init the socket at this port and address

guiworks.initwindow() #Init the window to the opening screen

guiworks.window.mainloop()
#Starts listening for connections, and when found it saves them to conn, and addrs










