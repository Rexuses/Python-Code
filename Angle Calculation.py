# Batuhan Beel
# Angle calculation
# 17.10.2020
def calculation_angle(hour,minute):
    hour_degree=360/12
    minute_degree=360/60
    add_degree_for_hour =360/(12*60)
    minute_hand_angle=minute*minute_degree # Calculate minute-hand angle
    hour_hand_angle=(hour*hour_degree)+(minute*add_degree_for_hour) # Calculate hour-hand angle
    angle=abs(minute_hand_angle-hour_hand_angle) # Calculate angle between hour-hand and minute hand.
    return angle


import time
import random
from datetime import datetime


while True :
    operator = input("Welcome to the angle calculation system between the hour and minute hands.\nPress 'q' to exit the system.\n1-Enter the time and calculate angle (manuel)\n2-Calculate the angle of current time\n:") # To determine which operator to use.
    if operator == "q":
        print("Logging Out...") # Exit message.
        time.sleep(1)
        break

    if operator == "1":
        while True:
            try:
                hour = int(input("Please enter the hour :")) # To get hour from user.
                if hour<24 and hour>=0:
                        minute = int(input("Please enter the minute :")) # To get minute from user.
                        if minute < 60 and minute >= 0:
                            if hour > 12:
                                hour = hour - 12
                            result=calculation_angle(hour,minute)
                            time.sleep(1)
                            print(result)
                            break
                        else:
                            print("Please enter minute between 0-60.") # Error message.
                            continue
                else:
                    print("Please enter hour between 0-24.") # Error message.
                    continue

            except:
                print("Please enter integer number.") # Error message.
                continue
        while True:
            ask = input("Press 'w' to continue,'q' to exit:")
            if   ask   == 'w':
                break
            elif ask == 'q':
                print("Logging Out...") # Exit message.
                time.sleep(1)
                exit()
            else:
                print("Please enter 'w' or 'q'.") # Error message.
                continue
    if operator == "2":
        while True:
            current_time=datetime.strftime(datetime.now(), "%X") # Get time to use datetime module
            piece=current_time.split(":")
            hour=int(piece[0])
            if hour>12:
                hour=hour-12
            minute=int(piece[1])
            result = calculation_angle(hour, minute)
            time.sleep(1)
            print(result)
            break
        while True:
            ask = input("Press 'w' to continue,'q' to exit:")
            if   ask   == 'w':
                break
            elif ask == 'q':
                print("Logging Out...") # Exit message.
                time.sleep(1)
                exit()
            else:
                print("Please enter 'w' or 'q'.") # Error message.
                continue

