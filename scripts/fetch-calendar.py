import csv
import json
import os
import ssl
import urllib.request

url = 'https://docs.google.com/spreadsheets/d/1bagngvlrVxUeXkDZBAFAyGr6D2IW4nBI/export?format=csv&gid=601385898'

os.makedirs('_data', exist_ok=True)

# Bypass SSL verification for local macOS environment
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

response = urllib.request.urlopen(url, context=ctx)
lines = [line.decode('utf-8') for line in response.readlines()]
reader = csv.DictReader(lines)

events = [row for row in reader if any(row.values())]

with open('_data/events.json', 'w', encoding='utf-8') as f:
  json.dump(events, f, ensure_ascii=False, indent=2)

print(
    f'Successfully fetched {len(events)} events and saved to _data/events.json'
)