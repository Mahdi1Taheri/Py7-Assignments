# this program converts second to hour and minute.(exp 3620sec => 1:00:20)

sec = int(input("Enter the second: "))

sec_hour = sec // 3600
sec_minute = (sec % 3600) // 60
second = (sec % 3600) % 60

print(f"{sec_hour}:{sec_minute}:{second}")