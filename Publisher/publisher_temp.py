import paho.mqtt.client as mqtt
import time
import random

student_id = "12220183"

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    temp = random.randint(20, 35)
    message = f"Temperature: {temp}C | ID: {student_id}"
    client.publish("iot/temp", message)
    print("Published:", message)

    with open("log_temp.txt", "a") as f:
        f.write(message + "\n")
    time.sleep(3)
