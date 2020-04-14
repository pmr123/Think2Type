from NeuroPy import NeruroPy as N
from time import sleep

# object1=N.NeuroPy("COM3",57600) 
neuropy = N.NeuroPy('COM3',57600)
neuropy.start()

while True:
    if neuropy.meditation > 70: # Access data through object
        print("here")
        neuropy.stop() 
    sleep(0.2) # Don't eat the CPU cycles