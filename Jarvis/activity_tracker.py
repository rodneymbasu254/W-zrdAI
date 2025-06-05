import time

def log_activity(activity):
    with open("activity_log.txt", "a") as f:
        f.write(f"{time.ctime()}: {activity}\n")
