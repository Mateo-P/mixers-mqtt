import os
from dotenv import load_dotenv
import paho.mqtt.publish as publish
load_dotenv()

# Create an MQTT client and attach our routines to it.
mqttBroker = os.getenv('MQTT_BROKER')
port = int(os.getenv('PORT'))
mixer_id = os.getenv('MIXER_ID')
topic = f'mixer/{mixer_id}/recipes_request'

csv_recipes = open("mixer_recipes.csv", "r")
recipes = csv_recipes.readlines()
payload = ""
for recipe in recipes:
    payload += recipe
publish.single(topic, payload=payload,
               hostname=mqttBroker, port=port, keepalive=60)
print(f'Just published {payload} to Topic: mixer/{mixer_id}/recipes_request')
