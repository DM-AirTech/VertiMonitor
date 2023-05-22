# -*- coding: utf-8 -*-
"""
Company Name: DM-AirTech GmbH
Author: Harsh Panwar
Email: harsh@dm-airtech.com
Created on: Mon May 22 16:50:10 2023

Copyright (c) 2023, DM-AirTech GmbH

Description: This script, verti_monitor_integrate, serves as an integration module for the VertiMonitor API, enabling users to seamlessly incorporate VertiMonitor's robust data and features within their own Python applications.

The script includes functions to facilitate authentication, data retrieval, and processing using the VertiMonitor API, simplifying the process of sending requests to the API and handling responses.

Usage of this script requires a valid VertiMonitor API key, which can be obtained by contacting the VertiMonitor sales and support team. The API key is necessary to authenticate requests to the VertiMonitor API and to access its features.

Users of this script can integrate VertiMonitor's data directly into their Python applications, leveraging the power and flexibility of the VertiMonitor platform to enhance their own projects or products.

Please note that all interactions with the VertiMonitor API are subject to the terms and conditions of the API's usage policy.
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

def send_request(api_key, departure_time, arrival_time, aircraft_id, points, parameters=None):
    data = {
        "apiKey": api_key,
        "departureTime": departure_time,
        "arrivalTime": arrival_time,
        "aircraftId": aircraft_id,
        "points": points
    }
    
    if parameters is not None:
        data["parameters"] = {
            "wind": parameters[0],
            "rain": parameters[1],
            "temperature": parameters[2]
        }

    url = "https://www.dm-airtech.eu/api/VertiMonitorAPI"

    payload = json.dumps(data)
    headers = {
        'Content-Type': 'application/json',
        # 'Authorization': f'Bearer {api_key}' make it work for frontend as well
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        print("Request submitted successfully. API response:\n", response.text)
    else:
        print("Request failed with status code", response.status_code)


