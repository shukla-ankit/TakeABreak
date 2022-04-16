import json
import time
from datetime import datetime
from tkinter import *
from tkinter import ttk
from typing import List

class GUIManager:
    def __init__(self) -> None:
        self.root = None
        self.is_break_time = False
        self.is_reminder_snoozed = False
        
    def snooze(self):
        self.is_reminder_snoozed = True
        self.root.destroy()

    def start_break(self):
        self.is_reminder_snoozed = False
        self.is_break_time = True
        self.root.destroy()

    def end_break(self):
        self.is_break_time = False
        self.root.destroy()
    
    def start_break_reminder(self):
        self.root = Tk()
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()
        ttk.Label(frm, text="Take a break!\
            \n - walk around\
            \n - drink water\
            \n - stretch\
            \n - relax your eyers\
            \n\nCome back in 5 minutes..\n").grid(column=0, row=0)
        ttk.Button(frm, text="Start", command=self.start_break).grid(column=0, row=1)
        ttk.Button(frm, text="Snooze", command=self.snooze).grid(column=1, row=1)
        self.root.mainloop()

    def end_break_reminder(self):
        self.root = Tk()
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()
        ttk.Label(frm, text="Time to get back!\n").grid(column=0, row=0)
        ttk.Button(frm, text="Hide", command=self.end_break).grid(column=0, row=1)
        self.root.mainloop()


def time_unit_convertor( unit : str) -> int:
    one_second = 1
    one_minute = 60 * one_second
    one_hour = 60 * one_minute
    time_unit_to_seconds = {
        "second" : one_second,
        "seconds" : one_second,
        "minute": one_minute,
        "minutes": one_minute,
        "hour" : one_hour,
        "hours" : one_hour
    }
    return time_unit_to_seconds[unit]

def timestamp(message : str):
    print(message + str(datetime.now())[0:-7])

def read_config(config_info : List) :
    config_file_path = "config.json"
    info_json = json.load(open(config_file_path))
    time_unit = time_unit_convertor(info_json["time_unit"])
    config_info.append(info_json["work_duration"] * time_unit)
    config_info.append(info_json["break_duration"] * time_unit)
    config_info.append(info_json["snooze_duration"] * time_unit)

def main():
    config_info = []
    read_config(config_info)
    work_duration, break_duration, snooze_duration = config_info[0], config_info[1], config_info[2]
    gui = GUIManager()
    while True:
        time.sleep(work_duration)            
        while True:
            timestamp("Break message displayed @ ")
            gui.start_break_reminder()
            if gui.is_break_time:
                break
            if gui.is_reminder_snoozed:
                timestamp("Snooze @ ")
                time.sleep(snooze_duration)
        
        timestamp("\n-----------------------------------------------\nBreak started @ ")
        break_start_time = datetime.now()
        time.sleep(break_duration)
        gui.end_break_reminder()
        while gui.is_break_time:
            continue
        timestamp("Break ended @ ")
        break_end_time = datetime.now()
        actual_break_duration = break_end_time - break_start_time
        print("Break duration was " + str(actual_break_duration.seconds // 60) +  " minutes and " + str(actual_break_duration.seconds % 60) + " seconds.")
        print("-----------------------------------------------\n")

if __name__ == "__main__":
    main()

