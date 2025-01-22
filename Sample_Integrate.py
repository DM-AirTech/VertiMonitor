# -*- coding: utf-8 -*-
"""
Company Name: DM-AirTech GmbH
Author: Dario Milani
Email: dario@dm-airtech.com
Updated on: Wed Jan 2025 16:45:06 2023

Copyright (c) 2025, DM-AirTech GmbH

Description: This script, Sample_integrate.py, serves as an integration module for the VertiMonitor API, 
enabling users to seamlessly incorporate VertiMonitor's robust data and features within their own Python applications.
The script includes functions to facilitate authentication, data retrieval, and processing using the VertiMonitor API, 
simplifying the process of sending requests to the API and handling responses.
Usage of this script requires a valid VertiMonitor API key, which can be obtained by contacting the VertiMonitor sales and support team. 
The API key is necessary to authenticate requests to the VertiMonitor API and to access its features.
Users of this script can integrate VertiMonitor's data directly into their Python applications, 
leveraging the power and flexibility of the VertiMonitor platform to enhance their own projects or products.
Please note that all interactions with the VertiMonitor API are subject to the terms and conditions of the API's usage policy.
"""

import json
import requests
import uuid

def parse_point(point_str):
    point_data = point_str.split(',')
    return {
        "point": point_data[0],
        "Latitude": float(point_data[1]),
        "Longitude": float(point_data[2]),
        "altitude": int(point_data[3])
    }

def send_request(api_key, mode, model, start_time, end_time, aircraft_id, points, parameters=None):
    random_uuid = uuid.uuid4()
    data = {
        "ApiKey": api_key,
        "uuid": str(random_uuid),
        "mode": mode,
        "model": model,
        "startTime": start_time,
        "endTime": end_time,
        "aircraftId": aircraft_id,
        "points": points
    }
    
    if parameters is not None:
        data["parameters"] = {
            "wind": parameters[0],
            "rain": parameters[1],
            "temp_min": parameters[2],
            "temp_max": parameters[3]
        }

    url = "https://www.dm-airtech.eu/api/VertiMonitorAPI"

    payload = json.dumps(data)
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
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


