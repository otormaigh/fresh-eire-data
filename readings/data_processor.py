import json
import os
import sys

file = open(os.path.join(sys.path[0], 'raw.json'))
data = json.load(file)

with open(os.path.join(sys.path[0], 'raw.json')) as raw:
    raw_readings = json.load(raw)

with open(os.path.join(sys.path[0], 'latest.json')) as latest:
    latest_readings = json.load(latest)

for raw_reading in raw_readings:
    latest_readings.append(raw_reading['latest_reading'])

with open(os.path.join(sys.path[0], 'latest.json'), 'w') as f:
    f.write(json.dumps(latest_readings))
