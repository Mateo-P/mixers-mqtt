import os
from dotenv import load_dotenv
import paho.mqtt.publish as publish
load_dotenv()

# Connection to mqtt-broker
mqttBroker = os.getenv('MQTT_BROKER')
port = int(os.getenv('PORT'))


def send_recipe_to_mixer(recipe="PRUEBADESPUES;100;200;300;144;123;321;222;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;", mixer_id=1):
    topic = f'mixer/{mixer_id}/newrecipe'
    publish.single(topic, payload=recipe, hostname=mqttBroker,
                   port=port, keepalive=60)
    print(f'Just published {recipe} to Topic mixer/{mixer_id}/newrecipe')


send_recipe_to_mixer()
