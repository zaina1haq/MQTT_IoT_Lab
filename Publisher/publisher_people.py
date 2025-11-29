import paho.mqtt.client as mqtt
import time
import random

student_id = "12220183"

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    people = random.randint(0, 30)
    message = f"People Count: {people} | ID: {student_id}"
    client.publish("iot/people", message)
    print("Published:", message)
    
    with open("log_people.txt", "a") as f:
        f.write(message + "\n")
    time.sleep(3)
