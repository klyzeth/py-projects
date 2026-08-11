import time

countdown = int(input("Enter the countdown time: "))

for x in range(countdown, 0, -1):
    seconds = x % 60
    print(f"00:00:{seconds:02}")
    time.sleep(1)
print("Time's UP!")
