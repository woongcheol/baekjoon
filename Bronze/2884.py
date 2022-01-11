from datetime import datetime
import time

H, M = input().split()
time_1 = datetime.strptime(f"{H}:{M}", "%H:%M")
time_2 = datetime.strptime("00:45", "%H:%M")
print(time.strftime('%H %M', time_2))
# time_3 = time_1 - time_2

# print(time_1)