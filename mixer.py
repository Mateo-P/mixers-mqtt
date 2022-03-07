import paho.mqtt.client as mqtt
MIXER_ID = 1


def on_message(client, userdata, message):
    logOut = open("mixer_recipes.csv", "a", newline='')
    print(message.payload)
    logOut.write(str(message.payload.decode("utf-8")) + "\n")
    logOut.close()


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True  # set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


mqttBroker = "127.0.0.1"
client = mqtt.Client(str(MIXER_ID))
client.on_connect = on_connect
client.connect(mqttBroker)

client.subscribe(f'mixer/{MIXER_ID}/#', 2)
client.on_message = on_message
client.loop_forever()
