import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    logOut = open(f'{message.topic}.csv',"a",newline='')
    print(message.payload)
    logOut.write(str(message.payload.decode("utf-8"))+ "\n")
    logOut.close()

#Connection to mqtt-broker
mqttBroker = "127.0.0.1"
client = mqtt.Client("django_server")
client.connect(mqttBroker)

# methods
def send_recipe_to_mixer(recipe="MMGV;100;200;300;144;123;321;222;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;", mixer_id=1):
    client.publish(f'mixer/{mixer_id}/newrecipe', recipe,2)
    print("Just published " + str(recipe) + " to Topic mixer/"+mixer_id)

# Loop to receive messages trought subscriptons
client.loop_start()
client.subscribe("mixer/+/recipes_request",2)
client.on_message = on_message
client.loop_forever()
