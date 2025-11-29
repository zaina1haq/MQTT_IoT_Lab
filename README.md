# MQTT IoT Lab – Multiple Publishers & Subscribers  
This project is a simulation of an IoT system using the MQTT protocol.  
It demonstrates how different IoT sensors (Temperature, Humidity, and People Counter) send data using MQTT Publishers, and how different systems receive data using MQTT Subscribers.

The project uses:
- **Mosquitto MQTT Broker**
- **Paho MQTT Client (Python)**
- **Multiple Topics with Multiple Publisher/Subscriber pairs**
- **Random sensor values to simulate real IoT devices**

---

## 📡 Project Architecture

Each simulated IoT sensor has:
- **One Publisher** → sends messages  
- **One Subscriber** → receives only its topic  

Topics used:
- `iot/temperature`
- `iot/humidity`
- `iot/people`

This creates three independent IoT communication channels.

---

## 🚀 Features

✔ Three separate publishers (Temperature, Humidity, People Counter)  
✔ Three separate subscribers  
✔ MQTT communication through Mosquitto Broker  
✔ Random sensor data generation  
✔ Each message contains the student's ID  
✔ Continuous real-time message streaming  
✔ Clear terminal logs for both Publisher & Subscriber  

---

## 📁 Project Structure
MQTT_IoT_Lab/
│
├── Publisher/
│ ├── publisher_temp.py
│ ├── publisher_humidity.py
│ └── publisher_people.py
│
├── Subscribers/
│ ├── subscriber_temp.py
│ ├── subscriber_humidity.py
│ └── subscriber_people.py
│
└── README.md
---
## ▶️ How to Run the Project
 1 — Start Mosquitto Broker
 mosquitto
 
Step 2 — Run Subscribers (in separate terminals)
Temperature Subscriber:
python Subscribers/subscriber_temp.py

Humidity Subscriber:
python Subscribers/subscriber_humidity.py

People Counter Subscriber:
python Subscribers/subscriber_people.py

Step 3 — Run Publishers (in separate terminals)
Temperature Publisher:
python Publisher/publisher_temp.py

Humidity Publisher:
python Publisher/publisher_humidity.py

People Counter Publisher:
python Publisher/publisher_people.py


📥 Example Output

Temperature Publisher:
Published: Temperature: 25°C | ID: 12220183
Published: Temperature: 28°C | ID: 12220183

Temperature Subscriber:
Temp Subscriber Received: Temperature: 25°C | ID: 12220183
Temp Subscriber Received: Temperature: 28°C | ID: 12220183

📊 Sensor Simulation
Since this project uses simulated sensors, all readings are generated using Python’s random.randint().
This allows realistic IoT behavior without physical hardware:
Temperature changes dynamically
Humidity changes dynamically
People Counter increases/decreases

