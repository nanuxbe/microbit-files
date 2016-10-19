from microbit import *

while True:
    if button_a.is_pressed():
        pin1.write_digital(1)
        pin2.write_digital(1)
        pin0.write_digital(0)
        pin8.write_digital(0)
        display.show(Image.ARROW_N)
    elif button_b.is_pressed():
        pin0.write_digital(1)
        pin8.write_digital(1)
        pin1.write_digital(0)
        pin2.write_digital(0)
        display.show(Image.ARROW_S)
    else:
        pin0.write_digital(0)
        pin8.write_digital(0)
        pin1.write_digital(0)
        pin2.write_digital(0)
        display.show(Image.NO)
