import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(f'mixer/+/recipes_request', 2)


def on_message(client, userdata, message):
    parsed_csv_name = message.topic.replace('/', '-')
    logOut = open(f'{parsed_csv_name}.csv', "a", newline='')
    print(message.payload.decode("utf-8"))
    logOut.write(message.payload.decode("utf-8"))
    logOut.close()


# Connection to mqtt-broker
mqttBroker = "test.mosquitto.org"
port = 1883
client = mqtt.Client("django_server")
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqttBroker, port, 60)
client.loop_forever()
