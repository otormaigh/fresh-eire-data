import json
import os
import sys

file = open(os.path.join(sys.path[0], 'raw.json'))
data = json.load(file)

with open(os.path.join(sys.path[0], 'raw.json')) as file:
    raw_readings = json.load(file)


with open(os.path.join(sys.path[0], 'latest.json')) as file:
    latest_readings = json.load(file)


with open(os.path.join(sys.path[0], 'stations.json')) as file:
    stations = json.load(file)



for raw_reading in raw_readings:
    latest_readings.append(raw_reading['latest_reading'])

    stations.append({ 'monitor_id': raw_reading['monitor_id'], 'location': raw_reading['location'], 'latitude': raw_reading['latitude'], 'longitude': raw_reading['longitude'], 'num_readings': raw_reading['num_readings'], 'current_rating': raw_reading['current_rating'] })



with open(os.path.join(sys.path[0], 'latest.json'), 'w') as f:
    f.write(json.dumps(latest_readings))


with open(os.path.join(sys.path[0], 'stations.json'), 'w') as f:
    f.write(json.dumps(stations))
