import requests
import json

url = "https://api.ecmwf.int/v1"

params = {
    "dataset": "cera20c",
    "stream": "an",
    "levtype": "sfc",
    "param": "sst",
    "date": "1980-01-01/to/1980-01-31",
    "area": "70/-130/50/-110",
    "format": "netcdf",
    "time": "00:00:00",
    "target": "output.nc",
    "grid": "0.25/0.25",
    "key": "YOUR_API_KEY"
}

response = requests.get(url, params=params)

print(response.content)

# Decode the byte code into a JSON object
json_data = json.loads(response.content.decode("utf-8"))

# Write the JSON object to a file
with open("output.json", "w") as outfile:
    json.dump(json_data, outfile)

