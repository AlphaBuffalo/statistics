import requests as requests
import json
import sys


def main():
    latest = requests.get('https://api.weather.gov/stations/KMIA/observations/latest', params='require_qc=false')
    temperature = json.dumps(latest.json()['properties']['maxTemperatureLast24Hours'], indent=4)
    print(temperature)


if True:
    main()