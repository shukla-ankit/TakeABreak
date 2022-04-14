import os
import json
import time
from datetime import datetime
from BreakManager import BreakManager
from utils import utils

def main():
    # if os.name == "posix" or os.name == "darwin":
    #     config_file_path = "../config/config.json"
    # elif os.name == "nt":
    #     config_file_path = "..\\config\\config.json"
    # else:
    #     print('Unknown OS')
    #     exit()

    config_file_path = "config.json"
    info_json = json.load(open(config_file_path))
    time_unit = utils.time_unit_convertor(info_json["time_unit"])

    work_duration = info_json["work_duration"] * time_unit
    break_duration = info_json["break_duration"] * time_unit
    snooze_duration = info_json["snooze_duration"] * time_unit

    b = BreakManager()
    while True:
        time.sleep(work_duration)            
        while True:
            utils.timestamp("Break message displayed @ ")
            b.displayBreakStart()
            if b.snooze:
                utils.timestamp("Snooze @ ")
                time.sleep(snooze_duration)
            if b.start:
                break
        utils.timestamp("\n-----------------------------------------------\nBreak started @ ")
        break_start = datetime.now()
        time.sleep(break_duration)
        utils.timestamp("Break end message displayed @ ")
        b.displayBreakEnd()
        while b.start:
            continue
        utils.timestamp("Break ended @ ")
        break_end = datetime.now()
        actual_break_duration = break_end - break_start
        print("Break duration was " + str(actual_break_duration.seconds // 60) +  " minutes and " + str(actual_break_duration.seconds % 60) + " seconds.")
        print("-----------------------------------------------\n")

if __name__ == "__main__":
    main()

