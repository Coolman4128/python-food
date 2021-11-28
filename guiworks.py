from os import times
import tkinter as tk
import commands
import socketworks
import time

def initwindow():
    
    window.rowconfigure([0,1], minsize=100, weight=1)
    window.columnconfigure(0, minsize=500, weight=1)

    lbl_title.grid(row=0, column=0)
    btn_listen.grid(row=1,column=0)

def makeHome():
    pass

def startlisten():
    lbl_title.configure(font=('Arial, 25'))
    holdtup = socketworks.listenconn()
    lbl_title.configure(text= "Found Connection at " + holdtup[0])
    time.sleep(1)
    makeHome()

window = tk.Tk()
btn_listen = tk.Button(master=window, text="Start Listening", font=('Arial, 25'), command=startlisten)
lbl_title = tk.Label(master=window, text="Python-Food", font=('Arial, 40'))




