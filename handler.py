import requests
import xml.etree.ElementTree as ET
import os
import boto3

location_id=os.getenv('locationId')
bbc_url = os.getenv('bbcUrl')
strong_wind_threshold = int(os.getenv('strongWindThreshold'))
phone_number = os.getenv('phoneNumber')

client = boto3.client('sns')

def send_text(phone_number, message):
    return client.publish(
        PhoneNumber=phone_number,
        Message=message,
        Subject='Winds are coming'
    )

def is_it_windy(event, context):

    bbc_response = requests.get(bbc_url + location_id)
    root = ET.fromstring(bbc_response.text)

    next_day = root.find("./channel/item/[link='https://www.bbc.co.uk/weather/" + location_id + "?day=1']")
    
    description = next_day.find("./description").text
    wind_speed_description = description.split(',')[3]
    split_wind_description = wind_speed_description.split(':')

    if split_wind_description[0].lstrip() != 'Wind Speed':
        send_text(
            phone_number,
            'It looks like the API format has changed, look into it!'
        )

    wind_speed = split_wind_description[1].replace('mph', ''). lstrip()

    if (int(wind_speed) >= strong_wind_threshold):
        send_text(
            phone_number,
            'Strong wind of ' + wind_speed + 'mph tomorrow, time to shore up your plants!'
        )

    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
