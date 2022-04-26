#Radpy
#Radionics Python Protocol
import random
from time import sleep
import sys

import secrets


def slow_type(string, delay=0.02):
    for n in string:
        print(n,end='')
        sys.stdout.flush()
        sleep(delay)
    print()
    sleep(2)

def Scan(target):
    #Creates a link to target and returns a handle to the link
    uuid = secrets.token_hex(6).upper()
    freq = random.randint(1,255)
    slow_type(f"Scan Unique Identifier:\t{uuid}")
    slow_type(f"Scan Frequency:\t{freq}")


def Banish():
    slow_type("Performing banishing ritual...")
    slow_type("*Visualizing a ball of light above your head*")
    slow_type("*The ball of light moves from the top of your head down to your feet*")
    slow_type("*the ball moves back up to your chest and moves to your left palm*")
    slow_type("*The ball intsensifies with energy*")
    slow_type("*The ball of light begins to move to the other palm intensifying in radiance as it gets closer*")
    slow_type("*The ball of light begins to link to the forign energy within your body / mind and spirit and draws this energy into itself*")
    slow_type("*The ball turns slightly black and then a pure white as it transmutes the energy from a negative vibration into that of harmony with youself*")
    slow_type("*The ball begins to fall into the ground where its energy is re-absorbed into the earth*")
    slow_type("The Ritual is Complete...")



slow_type("RADPY - Radionics Program",0.04)
print("")
Banish()

slow_type("Enter Witness:\t")
target = input("")
slow_type("*Adjusting Radio Dials*")
slow_type("*Rubbing Stickpad*")
slow_type("*A strong stick has been found*")
Scan(target)
slow_type("Enter to Shutdown the machine")
input("")
slow_type("*turning knobs to zero*")


