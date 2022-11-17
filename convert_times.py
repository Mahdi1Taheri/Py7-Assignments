# convert times project
# user will enter the hour, minutes and seconds, then the computer will convert them to seconds.

hour = int(input("Enter the hour: "))
minute = int(input("Enter the minute: "))
sec = int(input("Enter the seconds: "))

hour_sec = hour * 3600
minute_sec = minute * 60

print(f"{hour}h:{minute}min:{sec}sec in second is: {hour_sec + minute_sec}sec")