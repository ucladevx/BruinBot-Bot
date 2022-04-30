import asyncio
from gpiozero import LED
from time import sleep
red = LED(26) #up
green = LED(6) #down
yellow = LED(19) #left
blue = LED(13) #right
state = "off"

def control(msg):
	state = msg

async def loop():
    while True:
        print(state)
        if (state == "up"):
            green.off()
            yellow.off()
            blue.off()
            red.on()
        elif (state == "right"):
            red.off()
            green.off()
            yellow.off()
            blue.on()
        elif (state == "down"):
            red.off()
            yellow.off()
            blue.off()
            green.on()
        elif (state == "left"):
            red.off()
            green.off()
            blue.off()
            yellow.on()
        elif (state == "off"):
            red.off()
            green.off()
            yellow.off()
            blue.off()
        elif (state == "break"):
            break
        else:
            print("not a state")

asyncio.get_event_loop().run_until_complete(loop())

   
