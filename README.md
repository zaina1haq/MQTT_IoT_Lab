╔═══════════════════════════════════════════════════════════╗
║           MQTT IoT Lab – Multiple Publishers & Subscribers      ║
║                   Student ID: 12220183                           ║
╚═══════════════════════════════════════════════════════════╝

Project Overview
────────────────
This project simulates a real-world IoT system using the MQTT protocol. 
Three different types of IoT sensors (Temperature, Humidity, and People Counter) 
continuously publish their data to a Mosquitto MQTT broker. 
Three dedicated subscribers listen to their respective topics and display 
the received data in real time.

The goal is to demonstrate:
• MQTT publish/subscribe architecture
• Topic-based message routing
• Multiple independent publisher/subscriber pairs
• Simulated sensor data without physical hardware
• Clean logging with student ID identification

Technologies Used
─────────────────
• MQTT Broker       : Eclipse Mosquitto
• MQTT Client Library: Paho-MQTT (Python)
• Language           : Python 3.x
• Random data generation for simulation

Topics Used
───────────
iot/temperature
iot/temperature
iot/humidity
iot/people

Each topic is completely independent – subscribers only receive messages 
from the topic they are subscribed to.

Project Structure
─────────────────
MQTT_IoT_Lab/
├── Publisher/
│   ├── publisher_temp.py      # Temperature sensor publisher
│   ├── publisher_humidity.py  # Humidity sensor publisher
│   └── publisher_people.py    # People counter publisher
├── Subscribers/
│   ├── subscriber_temp.py
│   ├── subscriber_humidity.py
│   └── subscriber_people.py
└── README.txt                 # This file

Features
────────
✓ 3 independent publishers
✓ 3 dedicated subscribers (one per topic)
✓ Real-time continuous data streaming
✓ Random but realistic sensor values
✓ Every message contains Student ID: 12220183
✓ Clear, color-coded console output
✓ Easy to extend with new sensors/topics

How to Run the Project
──────────────────────
1. Install requirements (one time)
   pip install paho-mqtt

2. Start the Mosquitto MQTT Broker (in its own terminal)
   mosquitto
   → Keep this terminal running!

3. Open 3 terminals and start the Subscribers
   python Subscribers/subscriber_temp.py
   python Subscribers/subscriber_humidity.py
   python Subscribers/subscriber_people.py

4. Open another 3 terminals and start the Publishers
   python Publisher/publisher_temp.py
   python Publisher/publisher_humidity.py
   python Publisher/publisher_people.py

→ You should now see real-time data flowing from publishers → broker → subscribers!

Example Output
──────────────
[Temperature Publisher]
Published → Topic: iot/temperature | Temperature: 24°C | ID: 12220183
Published → Topic: iot/temperature | Temperature: 27°C | ID: 12220183

[Temperature Subscriber]
Temp Subscriber Received → Temperature: 24°C | ID: 12220183
Temp Subscriber Received → Temperature: 27°C | ID: 12220183

Similar logs appear for Humidity and People Counter.

Sensor Simulation Details
────────────────────────
• Temperature   : 15–35 °C (random fluctuation)
• Humidity      : 30–90 %   (random fluctuation)
• People Counter: Incremental with occasional decrease (entering/leaving)

All values are generated using random.randint() and time.sleep() 
to mimic real sensor behavior.

Troubleshooting
───────────────
• Connection refused? → Make sure Mosquitto broker is running first!
• Port 1883 in use?   → Kill old Mosquitto instances:
    pkill mosquitto   (Linux/Mac) or Task Manager (Windows)
• Module not found?  → Run: pip install paho-mqtt
• No messages?       → Verify topic names are exactly the same in pub/sub

Submission Notes
────────────────
• All messages contain my Student ID: 12220183 for verification
• Screenshots of running publishers and subscribers are included in the repository
• Code is clean, commented, and follows PEP8

Enjoy the IoT simulation!

– Student ID: 12220183
  Date: November 2025
