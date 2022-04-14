import time
from tkinter import *
from tkinter import ttk
from datetime import datetime

class BreakManager:
    def __init__(self) -> None:
        self.snooze = False
        self.root = None
        self.snooze = False
        self.start = False
        
    def Snooze(self):
        self.snooze = True
        self.root.destroy()
        #self.root = None

    def Start(self):
        self.snooze = False
        self.start = True
        self.root.destroy()
        #self.root = None

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


def timestamp(message : str):
    print(message + str(datetime.now())[0:-7])

def main():
    seconds_in_minutes = 60
    one_minute = seconds_in_minutes
    work_duration = 55 * one_minute
    break_duration = 5 * one_minute
    snooze_duration = 2 * one_minute
    b = BreakManager()
    while True:
        time.sleep(work_duration)            
        while True:
            timestamp("Break message displayed @ ")
            b.displayBreakStart()
            if b.snooze:
                timestamp("Snooze @ ")
                time.sleep(snooze_duration)
            if b.start:
                break
        timestamp("\n-----------------------------------------------\nBreak started @ ")
        break_start = datetime.now()
        time.sleep(break_duration)
        timestamp("Break end message displayed @ ")
        b.displayBreakEnd()
        while b.start:
            continue
        timestamp("Break ended @ ")
        break_end = datetime.now()
        actual_break_duration = break_end - break_start
        print("Break duration was " + str(actual_break_duration.seconds // 60) +  " minutes and " + str(actual_break_duration.seconds % 60) + " seconds.")
        print("-----------------------------------------------\n")

if __name__ == "__main__":
    main()

