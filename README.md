Simple Alarm Clock
A basic console-based Alarm Clock built in Python as part of the TAE-I (Utility Assessment) project.
Overview
This utility allows a user to set an alarm time. It continuously monitors the system's current time, and when the current time matches the alarm time, it triggers an alert message notifying the user.
Features
Set an alarm using 24-hour format (HH:MM)
Continuously checks system time in the background
Displays an alert message when the alarm time is reached
How It Works (Logic)
set_alarm() — Takes alarm time input from the user.
check_time(alarm_time) — Runs a loop that checks the current system time every second and compares it with the alarm time.
trigger_alert() — Once the current time matches the alarm time, this function prints an alert message to notify the user.
Installation & How to Run
Make sure Python 3 is installed on your system.
Download or clone this repository.
Run the file using:
Enter the alarm time when prompted (format: HH:MM, 24-hour).
Wait for the alarm to trigger at the specified time.
Technologies Used
Python 3
Built-in time module
Author
Devyani
