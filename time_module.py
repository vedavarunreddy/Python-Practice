'''
Simple Timer calculator / stop watch.
'''

import time

def stop_watch():
    watch_option = input("Press 1 to start the stop watch. 0 to end: ")
    if watch_option == "1":
        while watch_option == "1":
            time_now = time.time()
            print("\nClock started! ")
            watch_option = input("Press 0 to end: ")
            if watch_option == "0":
                time_later = time.time()
                break
        time_passed = time_later - time_now
        time_passed = round(time_passed, 2)
        return time_passed
    else:
        return "Exception raised"

def points_calculator(seconds):
    try:
        if seconds < 10:
            points_scored = 3
        elif 10 <= seconds < 15:
            points_scored = 2
        else:
            points_scored = 1
        return points_scored
    except Exception:
        return Exception

running_time = stop_watch()
points_won = points_calculator(running_time)
print(f"You have won {points_won} points since you finished the race in {running_time} seconds.")
    