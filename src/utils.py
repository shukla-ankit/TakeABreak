import datetime

class utils:
    def timestamp(message : str):
        print(message + str(datetime.now())[0:-7])

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
