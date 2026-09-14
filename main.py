import time

print("SIMPLE ALARM CLOCK")

alarm_time = input("Enter alarm time (HH:MM): ")

print("Alarm set for:", alarm_time)
print("Waiting for alarm...")

while True:
    current_time = time.strftime("%H:%M")

    if current_time == alarm_time:
        print("ALARM! WAKE UP!")
        break

    time.sleep(1)
