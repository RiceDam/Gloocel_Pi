#Main python file for gloocel_pi 
from gpiozero import LED
from time import sleep 
import pika
import os 
from dotenv import load_dotenv

#Environment Variables
load_dotenv()

RMQ_USER = os.getenv('RMQ_USER')
PASS = os.getenv('PASS')
IP = os.getenv('IP')
PORT = os.getenv('PORT')

#GPIO port 18 assigned to led 
led_red = LED(18)

#GPIO port 17 assigned to led
led_green = LED(17)

#Doors that are assigned to queues
Queue1 = "TestQueue1"
Queue2 = "TestQueue2"

def main():

    credentials = pika.PlainCredentials(RMQ_USER, PASS)
    connection = pika.BlockingConnection(pika.ConnectionParameters(IP, PORT, '/', credentials))
    channel = connection.channel()

    #Callback method that takes in an led 
    def callback(body, led):
        print(" [x] Received %r" % body)
        message = body.decode("utf-8")
        if ('open' in message):
            led.on()
            sleep(5)
            led.off()
            print("Success, Opened Door")
        elif ('close' in message):
            led.off()
            print("Success, Closed Door")
        else:
            led.off()
            print("other")

    """
    Queue attribute needs to be changed when wanting to control a new door/queue
    First Queue/Door, controls RED led
    """
    channel.basic_consume(queue=Queue1, on_message_callback=lambda ch, method, properties, body: callback(body, led_red), auto_ack=True)

    #Second Queue/Door, controls GREEN led
    channel.basic_consume(queue=Queue2, on_message_callback=lambda ch, method, properties, body: callback(body, led_green), auto_ack=True)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    main()

