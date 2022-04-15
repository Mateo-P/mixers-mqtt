import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os
from dotenv import load_dotenv
import paho.mqtt.publish as publish
load_dotenv()


def send_recipes():
    print('sent')
    # Create an MQTT client and attach our routines to it.
    mqttBroker = os.getenv('MQTT_BROKER')
    port = int(os.getenv('PORT'))
    mixer_id = os.getenv('MIXER_ID')
    topic = f'mixer/{mixer_id}/recipes_request'

    csv_recipes = open("recipe.csv", "r")
    recipes = csv_recipes.readlines()
    payload = ""
    for recipe in recipes:
        payload += recipe
    publish.single(topic, payload=payload, hostname=mqttBroker,
                   port=port)
    print(
        f'Just published {payload} to Topic: mixer/{mixer_id}/recipes_request')


def on_created(event):
    print('created')
    send_recipes()


def on_deleted(event):
    print('deleted')


def on_modified(event):
    print('created')


def on_moved(event):
    print('moved')
    send_recipes()


if __name__ == "__main__":
    patterns = ["*.csv"]
    ignore_patterns = []
    ignore_directories = False
    case_sensitive = True
    event_handler = PatternMatchingEventHandler(
        patterns, ignore_patterns, ignore_directories, case_sensitive)
    event_handler.on_created = on_created
    # event_handler.on_deleted = on_deleted
    #event_handler.on_modified = on_modified
    event_handler.on_moved = on_moved
    path = './'

    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        print('monitoring')
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
