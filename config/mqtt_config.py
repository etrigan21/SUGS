import os

from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('MQTT_HOST')
PASSWORD = os.getenv('MQTT_PASSWORD')
USERNAME = os.getenv('MQTT_USERNAME')
PORT = int(os.getenv('MQTT_PORT'))