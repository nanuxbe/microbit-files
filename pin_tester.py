from microbit import *

PINS = [pin0, pin1, pin2, pin8, pin16]

while True:
    if button_a.is_pressed():
        display.show("1")
        for pin in PINS:
            pin.write_digital(1)
    else:
        display.show(Image.NO)
        for pin in PINS:
            pin.write_digital(0)