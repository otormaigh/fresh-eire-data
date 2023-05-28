import json
import os
import sys
import operator

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

    stations_dir = sys.path[0] + '/stations'
    if not os.path.exists(stations_dir):
        os.makedirs(stations_dir)

    all_stations_path = os.path.join(stations_dir, 'all_stations.json')
    if not os.path.exists(all_stations_path):
        with open(all_stations_path, 'a') as file:
            file.write('[]')

    with open(all_stations_path) as file:
        all_station_reading = json.load(file)

    station_reading_path = os.path.join(stations_dir, raw_reading['serial_number'] + '_' + raw_reading['location'].replace(' ', '-') + '.json')
    if not os.path.exists(station_reading_path):
        with open(station_reading_path, 'a') as file:
            file.write('[]')

    with open(station_reading_path) as file:
        station_reading = json.load(file)

    try:
        if not raw_reading['latest_reading']['recorded_at'] in map(operator.itemgetter('recorded_at'), station_reading):
            reading = { 
                'recorded_at': raw_reading['latest_reading']['recorded_at'], 
                'date': raw_reading['latest_reading']['date'], 
                'time': raw_reading['latest_reading']['time'], 
                'location': raw_reading['location'], 
                'pm10': raw_reading['latest_reading']['pm10'], 
                'pm2_5': raw_reading['latest_reading']['pm2_5'], 
                'no2': raw_reading['latest_reading']['no2'], 
                'o3': raw_reading['latest_reading']['o3'],
                'so2': raw_reading['latest_reading']['so2'],
                'co': raw_reading['latest_reading']['co'],
                'status': raw_reading['latest_reading']['status']
                }
            station_reading.append(reading)
            all_station_reading.append(reading)
    except Exception as e: 
        print(e)
        print(raw_reading['serial_number'])

    with open(station_reading_path, 'w') as file:
        file.write(json.dumps(station_reading))

    with open(all_stations_path, 'w') as file:
        file.write(json.dumps(all_station_reading))


with open(os.path.join(sys.path[0], 'latest.json'), 'w') as f:
    f.write(json.dumps(latest_readings))


with open(os.path.join(sys.path[0], 'stations.json'), 'w') as f:
    f.write(json.dumps(stations))
