from microbit import *
import random
import radio

STATES = {
  0: "green",
  1: "red",
}

state = 0
display.clear()
radio.on()

while True:
    incoming = radio.receive()
    if incoming == "red":
        state = 1
    elif incoming == "green":
        sleep(random.randint(100, 500))
        incoming = radio.receive()
        if incoming != "red":
            state = 0
            radio.send("red")
    elif button_a.get_presses() > 0 or button_b.get_presses() > 0:
        state = 1 - state
        radio.send(STATES[1 - state])
        
    
    if STATES[state] == "red":
        pin0.write_digital(0)
        display.show(Image.NO)
    else:
        display.clear()
        pin0.write_digital(1)