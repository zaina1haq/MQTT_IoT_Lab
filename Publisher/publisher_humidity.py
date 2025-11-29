import paho.mqtt.client as mqtt
import time

student_id = "12220183"

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    humidity = 60
    message = f"Humidity: {humidity}% | ID: {student_id}"
    client.publish("iot/humidity", message)
    print("Published:", message)
    time.sleep(3)
