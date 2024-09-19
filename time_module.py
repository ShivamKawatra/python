import time
print(time.time()) #seconds completed from 1970

print(4)
time.sleep(5) #for wait during printing next line
print("This will print after 5 sec.")

t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
print(time.strftime("%b %d %Y %H:%M:%S", t)) #to print localtime
