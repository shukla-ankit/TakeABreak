import time
from tkinter import *
from tkinter import ttk

def display():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Take a break!\
        \n - walk around\
        \n - drink water\
        \n - stretch\
        \n - relax your eyers\
        \n\nCome back in 5 minutes..\n").grid(column=0, row=0)
    ttk.Button(frm, text="Hide", command=root.destroy).grid(column=0, row=1)
    root.mainloop()

def main():
    work_duration = 55 * 60
    while True:
        time.sleep(work_duration)
        display()

if __name__ == "__main__":
    main()
