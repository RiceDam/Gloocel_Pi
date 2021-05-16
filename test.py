#Test file for  testing led control 

from gpiozero import LED
from time import sleep 

#GPIO port 18 assigned to led 
led_red = LED(18)
#GPIO port 17 assigned to led
led_green = LED(17)


def main():

    #Flashes after every 1 second 
    #while True:
        # led_red.on()
        # led_red.off()
        # led_red.on()
        # sleep(1)
        # led_red.off()
        # led_green.on()
        # sleep(1)
        # led_green.off()
        # sleep(1)
        # led_red.on()
        # led_green.off()
        # sleep(1)
        
if __name__ == "__main__":
    main()

