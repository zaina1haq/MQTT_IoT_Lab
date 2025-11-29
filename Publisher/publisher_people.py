import paho.mqtt.client as mqtt
import time

student_id = "12220183"

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    people = random.randint(0, 30)
    message = f"People Count: {people} | ID: {student_id}"
    client.publish("iot/people", message)
    print("Published:", message)
    time.sleep(3)
