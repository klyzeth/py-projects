import time

countdown = int(input("Enter the countdown time: "))

for x in range(1, countdown + 1):
    print(x)
    time.sleep(1)
print("Time's UP!")
