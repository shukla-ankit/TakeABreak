from tkinter import *
from tkinter import ttk


class BreakManager:
    def __init__(self) -> None:
        self.snooze = False
        self.root = None
        self.snooze = False
        self.start = False
        
    def Snooze(self):
        self.snooze = True
        self.root.destroy()

    def Start(self):
        self.snooze = False
        self.start = True
        self.root.destroy()

    def EndBreak(self):
        self.start = False
        self.root.destroy()
    
    def displayBreakEnd(self):
        self.root = Tk()
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()
        ttk.Label(frm, text="Time to get back!\n").grid(column=0, row=0)
        ttk.Button(frm, text="Hide", command=self.EndBreak).grid(column=0, row=1)
        self.root.mainloop()

    def displayBreakStart(self):
        self.root = Tk()
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()
        ttk.Label(frm, text="Take a break!\
            \n - walk around\
            \n - drink water\
            \n - stretch\
            \n - relax your eyers\
            \n\nCome back in 5 minutes..\n").grid(column=0, row=0)
        ttk.Button(frm, text="Start", command=self.Start).grid(column=0, row=1)
        ttk.Button(frm, text="Snooze", command=self.Snooze).grid(column=1, row=1)
        self.root.mainloop()

