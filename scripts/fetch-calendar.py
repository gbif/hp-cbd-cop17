import csv
import json
import os
import urllib.request

url = 'https://docs.google.com/spreadsheets/d/1bagngvlrVxUeXkDZBAFAyGr6D2IW4nBI/export?format=csv&gid=601385898'

os.makedirs('_data', exist_ok=True)

response = urllib.request.urlopen(url)
lines = [line.decode('utf-8') for line in response.readlines()]
reader = csv.DictReader(lines)

events = [row for row in reader if any(row.values())]

with open('_data/events.json', 'w', encoding='utf-8') as f:
  json.dump(events, f, ensure_ascii=False, indent=2)