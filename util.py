import time

def time_generator():
    current_time = time.localtime()
    time_format = "{:02d}{:02d}{:02d}_{:02d}{:02d}"#{:02d}"
    file_time = time_format.format(
        current_time.tm_year % 100,
        current_time.tm_mon,
        current_time.tm_mday,
        current_time.tm_hour,
        current_time.tm_min,
        #current_time.tm_sec
    )
    return file_time
