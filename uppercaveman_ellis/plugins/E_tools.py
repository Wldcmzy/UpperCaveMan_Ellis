import time

def form_time_string(start = 0, end = 4):
    ret = ''
    for each in time.localtime()[start : end]:
        ret += str(each)
    return ret