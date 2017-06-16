import time
import calendar

ticks = time.time()
print "Number of Ticks since 1/1/70 at midnight: ", ticks

localtime = time.localtime(time.time())
print localtime

formattedtime = time.asctime(time.localtime(time.time()))
print formattedtime

cal = calendar.month(2017, 10)
print cal
