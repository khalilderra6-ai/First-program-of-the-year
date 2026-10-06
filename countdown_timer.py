import time 

time.sleep(3)

my_time = int(input("Enter the time in seconds : "))
for x in range (my_time, 0, -1) :
    hour = int(x/3600)%60
    minutes = int(x/60)
    second = x % 60
    print(f"{hour :02}:{minutes :02}:{second :02}")
    time.sleep(1)


print("Time's up ")

