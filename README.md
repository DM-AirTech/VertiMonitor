# VertiMonitor<sup>GWC</sup>

![Python](https://img.shields.io/badge/Python-3-blue)
![Version](https://img.shields.io/badge/Version-0.1-blue)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://uk.linkedin.com/company/dm-airtech)
[![Website](https://img.shields.io/website?up_message=online&url=https%3A%2F%2Fwww.dm-airtech.com/)](https://www.dm-airtech.com/)


![image](https://github.com/DM-AirTech/VertiMonitor/assets/40840002/2df6781b-5cf0-45a9-b0ac-833df1412788)


## 1. Introduction
VertiMonitor<sup>GWC</sup> is a real-time weather clearance tool developed by DM-AirTech (DMAT) that assists in the execution and automation of drone and eVTOL operations. It bases go/no-go decisions on hyperlocal weather conditions, supporting you in your flight operations. VertiMonitor<sup>GWC</sup> comes with a user-friendly Graphical User Interface (GUI) and can be easily integrated into your system through our seamless API.

Note: This GitHub repository focuses on the API of VertiMonitor<sup>GWC</sup>. For access to the GUI, please visit our website directly.

![image](https://github.com/DM-AirTech/VertiMonitor/assets/40840002/2c036340-58b9-44ef-b2ca-6f09a1174b89)


## 2. Obtaining API Key

To access the VertiMonitor<sup>GWC</sup> data through the API, you will need an API key. Please contact our sales team at info@dm-airtech.com to obtain your API key.

## 3. Usage

There are four different ways to access VertiMonitorGWC using our API based on your preference. Common parameters used are:

```YOUR_API_KEY: Your provided API key.
DEPARTURE_TIME: Departure time in the format YYYY-MM-DDTHH:mm.
ARRIVAL_TIME: Arrival time in the format YYYY-MM-DDTHH:mm.
AIRCRAFT_ID: Your aircraft ID. (Refer to aircraft_ids.csv)
Parameters (optional): WIND, RAIN, TEMPERATURE_RANGE
```

You can choose to provide both the Aircraft ID and the Parameters, or only the Aircraft ID (user-defined). If you choose to provide only the Aircraft ID, the Parameters will be autofilled from our database.

For detailed usage instructions, refer to the different methods listed below:

### Method 1: Command Line Interface (CLI)

With Aircraft ID and parameter

`python verti_monitor_CLI.py -k API_KEY -d DEPARTURE_TIME -a ARRIVAL_TIME -i AIRCRAFT_ID -p WIND RAIN TEMPERATURE_RANGE --points POINT1 POINT2 POINT3`

With only Aircraft ID

`python verti_monitor_CLI.py -k API_KEY -d DEPARTURE_TIME -a ARRIVAL_TIME -i AIRCRAFT_ID --points POINT1 POINT2 POINT3`

### Method 2: CLI with CSV file
1.	Create a CSV file (e.g., points.csv) with the following format:
```
point	latitude	longitude	altitude
1	51.505711	-0.195364	100
2	51.5067445	-0.185987	200
3	51.5170358	-0.0921961	100
```

2. Just like method 1 use the following terminal command with the exception of adding the csv file path.

With Aircraft ID and parameter

`python verti_monitor_CLI.py -k YOUR_API_KEY -d DEPARTURE_TIME -a ARRIVAL_TIME -i AIRCRAFT_ID -p WIND RAIN TEMPERATURE --csv /path/to/points.csv`

With only Aircraft ID

`python verti_monitor_CLI.py -k YOUR_API_KEY -d DEPARTURE_TIME -a ARRIVAL_TIME -i AIRCRAFT_ID --csv /path/to/points.csv`

### Method 3: Python integration
In your Python script, import verti_monitor_integrate and use the send_request function as shown in below:
```
import verti_monitor_integrate

api_key = "YOUR_API_KEY"
departure_time = "DEPARTURE_TIME"
arrival_time = "ARRIVAL_TIME"
aircraft_id = "AIRCRAFT_ID"
parameters = ("WIND", "RAIN", "TEMPERATURE")#optional

points = [
    {"point": "POINT_1", "latitude": LATITUDE_1, "longitude": LONGITUDE_1, "altitude": ALTITUDE_1},
    {"point": "POINT_2", "latitude": LATITUDE_2, "longitude": LONGITUDE_2, "altitude": ALTITUDE_2},
    {"point": "POINT_3", "latitude": LATITUDE_3, "longitude": LONGITUDE_3, "altitude": ALTITUDE_3}
]

verti_monitor_integrate.send_request(api_key, departure_time, arrival_time, aircraft_id, parameters, points)

```

### Method 4: CURL command
With Aircraft ID and parameter
```
curl --location "https://www.dm-airtech.eu/api/VertiMonitorAPI" --header "Content-Type: application/json" --data "{\"apiKey\": \"YOUR_API_KEY\", \"departureTime\": \"DEPARTURE_TIME\", \"arrivalTime\": \"ARRIVAL_TIME\", \"aircraftId\": \"AIRCRAFT_ID\", \"parameters\": {\"wind\": \"WIND\", \"rain\": \"RAIN\", \"temperature\": \"TEMPERATURE\"}, \"points\": [{\"point\": \"POINT_1\", \"latitude\": LATITUDE_1, \"longitude\": LONGITUDE_1, \"altitude\": ALTITUDE_1}, {\"point\": \"POINT_2\", \"latitude\": LATITUDE_2, \"longitude\": LONGITUDE_2, \"altitude\": ALTITUDE_2}, {\"point\": \"POINT_3\", \"latitude\": LATITUDE_3, \"longitude\": LONGITUDE_3, \"altitude\": ALTITUDE_3}]}"
```
With only Aircraft ID
```
curl --location "https://www.dm-airtech.eu/api/VertiMonitorAPI" --header "Content-Type: application/json" --data "{\"apiKey\": \"YOUR_API_KEY\", \"departureTime\": \"DEPARTURE_TIME\", \"arrivalTime\": \"ARRIVAL_TIME\", \"aircraftId\": \"AIRCRAFT_ID\",  \"points\": [{\"point\": \"POINT_1\", \"latitude\": LATITUDE_1, \"longitude\": LONGITUDE_1, \"altitude\": ALTITUDE_1}, {\"point\": \"POINT_2\", \"latitude\": LATITUDE_2, \"longitude\": LONGITUDE_2, \"altitude\": ALTITUDE_2}, {\"point\": \"POINT_3\", \"latitude\": LATITUDE_3, \"longitude\": LONGITUDE_3, \"altitude\": ALTITUDE_3}]}"
```

## 4. Output
The output format is the same for all the methods listed above. Here is an example:
```
{
    "result": "1",
    "rationale": "This flight is safe to schedule with Departure time of 2023-04-15T18:00 and Arrival time of 2023-04-15T19:00"
}
```
## Support

For any questions, concerns, or technical support, please reach out to our dedicated support team at info@dm-airtech.com. 

---

© 2023 DM-AirTech. All rights reserved.
