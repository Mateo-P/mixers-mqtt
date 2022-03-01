from email import message
import paho.mqtt.client as mqtt
MIXER_ID = '1'

def on_message(client, userdata, message):
    logOut = open("mixer_recipes.csv","a",newline='')
    print(message.payload)
    logOut.write(str(message.payload.decode("utf-8"))+ "\n")
    logOut.close()
  
#Connection to mqtt-broker
mqttBroker = "127.0.0.1"
client = mqtt.Client(MIXER_ID)
client.connect(mqttBroker)

# methods
def send_repices_to_server():
    csv_recipes = open("mixer_recipes.csv","r")
    recipes =  csv_recipes.readlines()
    for recipe in recipes:
        print(recipe)
    client.publish(f'mixer/{MIXER_ID}/recipes_request', recipes,2)
    print("Just published " + str(recipe) + " to Topic mixer/"+MIXER_ID)

# Loop to receive messages trought subscriptons
client.loop_start()
client.subscribe(f'mixer/{MIXER_ID}/#',2)
client.on_message = on_message
client.loop_forever()
