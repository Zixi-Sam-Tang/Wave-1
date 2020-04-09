import math
import time
print("Excercise 24:")
days = int(input())
hours = int(input())
min = int(input())
sec = int(input())
sec += days * 86400 + hours * 3600 + min * 60
print(sec)


print("Excercise 25:")
hour = ""
min = ""
sec = ""
secs = int(input())
days = math.floor(secs/86400)
secs -= days * 86400
hours = math.floor(secs/3600)
secs -= hours * 3600
mins = math.floor(secs/60)
secs -= mins * 60
if hours % 10 == hours:
    hour = "0" + str(hours)
else:
    hour = str(hours)
if mins % 10 == mins:
    min = "0" + str(mins)
else:
    min = str(mins)
if secs % 10 == secs:
    sec = "0" + str(secs)
else:
    sec = str(secs)
print(str(days) + " : " + hour + " : " + min + " : " + sec)


print("Excercise 26:")
print(time.asctime())