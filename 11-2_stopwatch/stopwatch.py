"""
Auth: Nate Koike
Proj: Stopwatch
Date: 10 November 2019
Desc: make a simple stopwatch
"""

import time

def get_time(sec):
    # get the hours
    hr = str(sec // 3600)

    # subtract the hours from the seconds
    sec -= int(hr) * 3600

    # get the minutes
    min = str(sec // 60)

    # subtract the minutes from the seconds
    sec -= int(min) * 60

    # make seconds a string
    sec = str(sec)

    # format the output for minutes
    if len(min) < 2:
        min = "0" + min

    # format the output for seconds
    if len(sec) < 2:
        sec = "0" + sec

    return [hr, min, sec]

def print_time(sec):
    # split the time appropriately
    time_list = get_time(sec)

    # print the hours
    print(time_list[0], end=":")

    # print the minutes
    print(time_list[1], end=":")

    # print the seconds
    print(time_list[2])

def main():
    sec = 0

    while True:
        time.sleep(1)
        sec += 1
        print_time(sec)

if __name__ == "__main__":
    main()
