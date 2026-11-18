#Computing time different
from datetime import datetime, timedelta
now = datetime.now()
then = datetime(2016, 5, 23)
delta = now - then
print(delta)
print(delta.days)
print(delta.seconds)
########################################
#Date object
########################################
#Time between two date-times
a = datetime(2016, 10, 6, 0,0,0)
b = datetime(2016, 10, 1, 23, 59, 59)

print(a-b)
print((a-b).days)
print((a-b).total_seconds())
############################################
