import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    decoded_msg = msg.payload.decode()
    print("Humidity Subscriber Received:", decoded_msg)
    
   
    with open("log_subscriber_humidity.txt", "a") as f:
        f.write(decoded_msg + "\n")

client = mqtt.Client()
client.connect("localhost", 1883, 60)

client.subscribe("iot/humidity")
client.on_message = on_message

client.loop_forever()
