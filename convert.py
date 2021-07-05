#!/usr/bin/env python
# Made by Charafeddine with alot of stackoverflow help :3
import csv
import re
import sys

if len(sys.argv) > 1:
    filename = str(sys.argv[1])
else:
    raise Exception("Give me an Input :')")

print("[--] Eating all the logs " + filename)
try:
    log_data = open(filename, "r")
except:
    raise Exception("Invalid Input ")

pattern = re.compile('(\w+)(?:=)(?:"{1,3}([\w\-\.:\ =]+)"{1,3})|(\w+)=(?:([\w\-\.:\=]+))')
events = []

for line in log_data:
    event = {}
    match = pattern.findall(line)
    for group in match:

        if group[0] != "":
            event[group[0]] = group[1]
        else:
            event[group[2]] = group[3]
    events.append(event)


headers = []
for row in events:
    for key in row.keys():
        if not key in headers:
            headers.append(key)

print("[--] Blasting everything into CSV")
newfilename = (filename.split(
    "/")[len(filename.split("/"))-1].split('.')[0])+'.csv'

with open(newfilename, 'w', newline='') as fileh:
    csvfile = csv.DictWriter(fileh, headers)
    csvfile.writeheader()
    for row in events:
        csvfile.writerow(row)
print("[--] Done - " + str(len(events)) + " rows written to " + newfilename)
