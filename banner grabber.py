
import requests
import time

target = input('Enter your target : ')
print("cullecting information about yor target")
print()
print("Please wait")

logic = requests.get(target)
time.sleep(2)
print("===========")
time.sleep(1)
print("====================")
time.sleep(0.5)
print("=================================")

print(logic.headers)
print("Happy Hacking")