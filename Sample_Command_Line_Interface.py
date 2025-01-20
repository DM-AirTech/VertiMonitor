# -*- coding: utf-8 -*-
"""
Company Name: DM-AirTech GmbH
Author: Harsh Panwar
Email: harsh@dm-airtech.com
Created on: Mon May 22 16:45:06 2023

Copyright (c) 2023, DM-AirTech GmbH

Description: verti_monitor_CLI is a command-line interface script that enables users to seamlessly interact with the VertiMonitor product. It serves as a convenient tool for users to execute VertiMonitor's functions and features directly from their terminal, bypassing the need for a graphical user interface.

It's designed to be user-friendly, and guides the user through the various functionalities of the VertiMonitor product, including real-time monitoring, data analysis, alerts, and much more.

To use verti_monitor_CLI, an API key is required. This key connects the CLI tool to the VertiMonitor product and verifies the user's access permissions. Users can obtain their API key by contacting our sales and support team. Our dedicated team is ready to assist users in setting up their CLI tool and addressing any questions or issues.
"""

import argparse
import json
import requests
import csv
import uuid



def parse_point(point_str):
    point_data = point_str.split(',')
    return {
        "point": point_data[0],
        "Latitude": float(point_data[1]),
        "Longitude": float(point_data[2]),
        "altitude": int(point_data[3])
    }

def main():
    parser = argparse.ArgumentParser(description="VertiMonitor API Request")
    parser.add_argument("-k", "--apiKey", required=True, help="API key")
    parser.add_argument("-m", "--mode", required=True, help="trajectory, volume or sensor")
    parser.add_argument("-md", "--model", required=True, help="gfs-global, metar, icon_global or icon_seamless")
    parser.add_argument("-d", "--startTime", required=True, help="Departure time (YYYY-MM-DDTHH:mm)")
    parser.add_argument("-a", "--endTime", required=True, help="Arrival time (YYYY-MM-DDTHH:mm)")
    parser.add_argument("-i", "--aircraftId", required=True, help="Aircraft ID")
    parser.add_argument("-p", "--parameters", nargs=4, metavar=("wind", "rain", "temp_min", "temp_max"), help="Parameters (wind, rain, temp_min. temp_max)", required=False)
    parser.add_argument("-c", "--csv", help="CSV file containing points (optional)")
    parser.add_argument("--points", nargs='+', help="Points in format: point,latitude,longitude,altitude (optional)")

    args = parser.parse_args()

    if args.parameters is None and args.aircraftId is None:
        parser.error("Either both -i and -p or just -i must be provided")

    points = []

    if args.csv:
        with open(args.csv, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                points.append({
                    "point": row["point"],
                    "Latitude": float(row["latitude"]),
                    "Longitude": float(row["longitude"]),
                    "altitude": int(row["altitude"])
                })
    elif args.points:
        for point_str in args.points:
            points.append(parse_point(point_str))

    # Generate a random UUID
    random_uuid = uuid.uuid4()
    
    data_new = {
        "ApiKey": args.apiKey,
        "uuid": str(random_uuid),
        "mode": args.mode,
        "model": args.model,
        "startTime": args.startTime,
        "endTime": args.endTime,
        "aircraftId": args.aircraftId,
        "parameters": {
            "wind": float(args.parameters[0]) if args.parameters else 10,
            "rain": float(args.parameters[1]) if args.parameters else 0,
            "temp_min": float(args.parameters[2]) if args.parameters else -6,
            "temp_max": float(args.parameters[3]) if args.parameters else 40,
        },
        "points": points
    }


    url = "https://www.dm-airtech.eu/api/VertiMonitorAPI"

    
    payload = json.dumps(data_new)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {args.apiKey}',
        'User-Agent': 'PostmanRuntime/7.43.0',
        'Accept': '*/*',
        'Postman-Token': '',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://dm-airtech.eu/api/VertiMonitorAPI',
        'Host': 'www.dm-airtech.eu'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        print(response.text)
    else:
        print("Request failed with status code", response.status_code)

if __name__ == "__main__":
    main()