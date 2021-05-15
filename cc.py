import cayenne.client
import time

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "cc19b960-9ded-xxxx-xxxx-3f1a8f1211ba"
MQTT_PASSWORD  = "b6f7930368322aefxxxxxxab38c52ff9bba1a"
MQTT_CLIENT_ID = "80839f80-9e64-xxxx-xxxx-b32ea624e442"

# The callback for when a message is received from Cayenne.
def on_message(message):
  print("message received: " + str(message))
  # If there is an error processing the message return an error string, otherwise return nothing.

client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message
#client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)
# For a secure connection use port 88803 when calling client.begin:
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, port=8883)

def reserve(i):
    client.loop()
    client.virtualWrite(i, 1, "digital_sensor", "d")
    
def empty(j):
    client.loop()
    client.virtualWrite(j, 0, "digital_sensor", "d")
