import paho.mqtt.client as mqtt
import time
import random

student_id = "12220183"

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    humidity = random.randint(40, 80)
    message = f"Humidity: {humidity}% | ID: {student_id}"
    client.publish("iot/humidity", message)
    print("Published:", message)
    
    with open("log_humidity.txt", "a") as f:
        f.write(message + "\n")
    time.sleep(3)
