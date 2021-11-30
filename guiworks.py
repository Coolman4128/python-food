from os import times
import tkinter as tk
from tkinter import font
import commands
import socketworks
import threading

def initwindow(): # Function for initing the opening window
    window.rowconfigure([0,1], minsize=100, weight=1) #Set the window up for the opening screen
    window.columnconfigure(0, minsize=500, weight=1)
    lbl_title.grid(row=0, column=0) # Place opening label and button on screen
    btn_listen.grid(row=1,column=0)

def makeHome():
    lbl_title.grid_remove() #Remove the Label and Button from the screen
    btn_listen.grid_remove()

    window.rowconfigure(0, minsize=50, weight=1) #Size top row for buttons to change menu you are in
    window.rowconfigure(1, minsize=500, weight=1) #Size middle row to hold everything needed
    window.rowconfigure(2, weight=1) #Size Bottom row to hold the status label
    window.columnconfigure(0, minsize=500, weight=1) #Size the only column

    #Setup the top row of the GUI
    frm_menubuttons.grid(row=0,column=0, sticky="w") #Grid the frame for the buttons then setup its columns and row
    frm_menubuttons.rowconfigure(0, minsize=50, weight=1)
    frm_menubuttons.columnconfigure([0,1], minsize=50)
    btn_comenu.grid(row=0,column=0,sticky="nsew")
    btn_termenu.grid(row=0,column=1,sticky="nsew")

    #Setup the Middle row to open to 
    frm_commbuttons.grid(row=1,column=0, sticky = "nsew")

    #Sertup the status row:
    lbl_status.grid(row=3,column=0,sticky="w")

def startlisten():
    lbl_title.configure(font=('Arial, 25')) # Change font of label
    socketworks.listenconn() # Listen for connections, and save the return into tuple named holdtup
    lbl_title.configure(text= "Found Connection at " + socketworks.conn.getAddress()) #Say where we found the connection
    timer = threading.Timer(3, makeHome)
    timer.start()

def buildFrames():
    #Code to build the Command Buttons Frame
    btn_mes.grid(row=0, column=0, padx=5, pady=5)

    #Code to build the Terminal Frame
    frm_terminal.rowconfigure(0, minsize=480, weight=1)
    lbl_terminal.grid(row=0, column=0, sticky="sw")
    ety_terminal.grid(row=1, column=0, sticky="sw")
    ety_terminal.insert(0, "Type Commands Here:")
    btn_sendterm.grid(row=1, column=1, sticky= "nsew")

def updateTerminal():
    terminalText = ety_terminal.get() #Grab the text in the entry and save it in terminalText
    newtext = "" #Will use this varible to store the new entry sent to the label
    if len(terminalLines) > 27: # Check to see if a line needs to go "offscreen"
        terminalLines.pop(0)
    terminalLines.append(terminalText) #Add new line into the list
    terminalLines[-2] = terminalLines[-2] + "\n" #I hate new lines 
    ety_terminal.delete(0, tk.END) #Clear the enrty for more commands
    for item in terminalLines: #Create a single string with all the lists entries
        newtext = newtext + item
    lbl_terminal.configure(text=newtext)  #Send the new text over
    

def swapComm():
    frm_terminal.grid_forget() #MUST BE GRID FORGET, PLEASE DONT FORGET AGAIN
    frm_commbuttons.grid(row=1,column=0, sticky = "nsew")

def swapTerm():
    frm_commbuttons.grid_forget()
    frm_terminal.grid(row=1,column=0, sticky = "nsew")


terminalLines = [" "]

#Assign all the elements that will be changed later outside of the function so they update
window = tk.Tk()

#Assign Frames Here:
frm_menubuttons = tk.Frame(master=window, width=500, height=50, bg="black")
frm_commbuttons = tk.Frame(master=window, bg = "black")
frm_terminal = tk.Frame(master=window, bg = "black")
frm_test = tk.Frame(master=window)

#Assign Buttons Here:
btn_listen = tk.Button(master=window, text="Start Listening", font=('Arial, 25'), command=startlisten)
btn_comenu = tk.Button(master = frm_menubuttons, text="C", font =('Arial, 15'), command= swapComm)
btn_termenu = tk.Button(master = frm_menubuttons, text="T", font =('Arial, 15'), command= swapTerm)
btn_mes = tk.Button(master=frm_commbuttons, text="Message", font=('Arial, 20'))
btn_sendterm = tk.Button(master=frm_terminal, text=">", font=('Arial, 10'), command=updateTerminal)

#Assign Labels Here:
lbl_title = tk.Label(master=window, text="Python-Food", font=('Arial, 40'))
lbl_status = tk.Label(master=window, text="Status = Idle", font=('Arial, 15'))
lbl_terminal = tk.Label(master = frm_terminal, text = "Start of the terminal:", font = ('Consolas, 10'), bg= "Black", fg="Green", justify="left")

#Assign Entries here:
ety_terminal = tk.Entry(master=frm_terminal, font=('Consolas, 10'), width=100)



