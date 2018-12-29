import time

print(time.time())
print("GM Time: ", time.gmtime())
print("Local Time: ",time.localtime())
t = time.localtime()
print("{}:{}, {}/{}/{}".format(t.tm_hour, t.tm_min, t.tm_mday, t.tm_mon, t.tm_year))
print(time.asctime())
print("Hello before the sleep")
time.sleep(5) #input is in seconds
print("HELLO wake up")
