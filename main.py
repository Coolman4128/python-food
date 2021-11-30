#RAT MADE USING PYTHON 

import commands
import socketworks
import guiworks

socketworks.initsocket('192.168.1.178', 15000) #Init the socket at this port and address

guiworks.initwindow() #Init the window to the opening screen

guiworks.buildFrames()

guiworks.window.mainloop() #Required for Tkninker events to be handled, meaning the rest of the functionality will be handled by tkninker functions.











