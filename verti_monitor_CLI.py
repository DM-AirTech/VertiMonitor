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

def parse_point(point_str):
    point_data = point_str.split(',')
    return {
        "point": point_data[0],
        "latitude": float(point_data[1]),
        "longitude": float(point_data[2]),
        "altitude": int(point_data[3])
    }

def main():
    parser = argparse.ArgumentParser(description="VertiMonitor API Request")
    parser.add_argument("-k", "--apiKey", required=True, help="API key")
    parser.add_argument("-d", "--departureTime", required=True, help="Departure time (YYYY-MM-DDTHH:mm)")
    parser.add_argument("-a", "--arrivalTime", required=True, help="Arrival time (YYYY-MM-DDTHH:mm)")
    parser.add_argument("-i", "--aircraftId", required=True, help="Aircraft ID")
    parser.add_argument("-p", "--parameters", nargs=3, metavar=("wind", "rain", "temperature"), help="Parameters (wind, rain, temperature)", required=False)
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
                    "point": row["points"],
                    "latitude": float(row["latitude"]),
                    "longitude": float(row["longitude"]),
                    "altitude": int(row["altitude"])
                })
    elif args.points:
        for point_str in args.points:
            points.append(parse_point(point_str))

    data_new = {
        "apiKey": args.apiKey,
        "departureTime": args.departureTime,
        "arrivalTime": args.arrivalTime,
        "aircraftId": args.aircraftId,
        "parameters": {
            "wind": args.parameters[0] if args.parameters else None,
            "rain": args.parameters[1] if args.parameters else None,
            "temperature": args.parameters[2] if args.parameters else None,
        },
        "points": points
    }


    url = "https://www.dm-airtech.eu/api/VertiMonitorAPI"

  
    payload = json.dumps(data_new)
    headers = {
        'Content-Type': 'application/json',
        # 'Authorization': f'Bearer {args.apiKey}' make it work for FrontEnd as well.
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        print("Request submitted successfully")
        print(response.text)
    else:
        print("Request failed with status code", response.status_code)

if __name__ == "__main__":
    main()
