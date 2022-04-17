import os
from dotenv import load_dotenv
import paho.mqtt.client as mqtt
load_dotenv()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    mixer_id = os.getenv('MIXER_ID')
    site_id = os.getenv('SITE_ID')
    client.subscribe(f'mixer/{mixer_id}/#', 2)

    client.subscribe(f'site/{site_id}/#', 2)

# The callback for when a PUBLISH message is received from the server.


def on_message(client, userdata, message):
    logOut = open("mixer_recipes.csv", "w", newline='')
    print(message.payload)
    logOut.write(str(message.payload.decode("utf-8")) + "\n")
    logOut.close()
    unmount = os.system('sudo modprobe -r g_mass_storage')
    print("`mount` ran with exit code %d" % unmount)
    mount = os.system(
        "sudo modprobe g_mass_storage file=/usb-drive.img stall=0 ro=0 removable=1")
    print("`mount` ran with exit code %d" % mount)


# Create an MQTT client and attach our routines to it.
mqttBroker = os.getenv('MQTT_BROKER')
port = int(os.getenv('PORT'))
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqttBroker, port, 60)
client.loop_forever()
