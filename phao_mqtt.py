import paho.mqtt.client as mqtt
import time

def on_msg(client,userdata,msg):
    print(str(msg.topic), msg.payload.decode('utf-8'))

def on_connect(client,userdata,flag,rc):
    print('Connected:',rc)

client = mqtt.Client()

client.on_message = on_msg
client.on_connect = on_connect

client.connect('test.mosquitto.org',1883)
client.loop_start()

subtop = input("\nEnter the subtopic:")
pubtop = input("\nEnter the pubtopic:")

client.subscribe(subtop)

while(1):
    chat = input("\nEnter your message:")
    if chat == 'q' :
        break
    else:
        client.publish(pubtop,chat)
    client.loop_stop()
