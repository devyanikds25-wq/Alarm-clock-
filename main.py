
import time

def set_alarm():
    return input("Enter alarm time (HH:MM): ")

def check_time(alarm_time):
    print("Alarm set for:", alarm_time)
    print("Waiting for alarm...")
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            print("Time matched!")
            break
        time.sleep(1)

alarm_time = set_alarm()
check_time(alarm_time)
