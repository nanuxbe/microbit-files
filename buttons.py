from microbit import button_a, button_b, pin0, pin1, sleep

while True:
    sleep(100)
    for (pin, button) in ((pin0, button_a), (pin1, button_b)):
        pin.write_digital(not button.is_pressed())
