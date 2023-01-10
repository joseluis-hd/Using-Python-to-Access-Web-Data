import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter location: ")
print("Retrieving", url)
data = urllib.request.urlopen(url).read().decode()
print("Retrieved", len(data), "characters")

try:
    js = json.loads(data)
except:
    js = None

count = 0
sum = 0

for item in js["comments"]:
    count += 1
    sum += int(item["count"])

print("Count: ", count)
print("Sum: ", sum)
