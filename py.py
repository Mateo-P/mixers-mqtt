try:
    import os
    from dotenv import load_dotenv
    import paho.mqtt.publish as publish
    load_dotenv()

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
    publish.single(topic, payload=payload,
                   hostname=mqttBroker, port=port, keepalive=60)
    print(
        f'Just published {payload} to Topic: mixer/{mixer_id}/recipes_request')
    clean_file = os.system('sudo rm recipe.csv')
    print("`rm` ran with exit code %d" % clean_file)
    unmount = os.system('sudo modprobe -r g_mass_storage')
    print("`unsmount` ran with exit code %d" % unmount)
    mount = os.system(
        "sudo modprobe g_mass_storage file=/usb-drive.img stall=0 ro=0 removable=1")
    print("`mount` ran with exit code %d" % mount)
except:
    print('tried to read csv but it doesnt exists')
