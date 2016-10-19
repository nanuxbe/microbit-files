import radio
from microbit import pin0, pin1, pin2, pin8, display, Image, sleep

ARROWS = {
    "backwards": Image.ARROW_S,
    "forwards": Image.ARROW_N,
    "left": Image.ARROW_W,
    "right": Image.ARROW_E,
}

DIRECTIONS = {
    "forwards":  (0, 1, 1, 0),
    "backwards": (1, 0, 0, 1),
    "left":      (1, 0, 1, 0),
    "right":     (0, 1, 0, 1),
}


radio.on()

while True:
    try:
        message = radio.receive()
    except ValueError:
        radio.off()
        sleep(100)
        radio.on()
        message = None

    direction = None
    if message is not None:
        data = message.split(":")
        if data[0] == "move":
            direction = data[1]

    if direction is not None:
        display.show(ARROWS[direction])
        pins = DIRECTIONS[direction]
        # to avoid shorting motors
        # first turn everything off then turn on the ones that need to be
        for value in range(2):
            for index, pin in enumerate([pin0, pin1, pin2, pin8]):
                if pins[index] == value:
                    pin.write_digital(value)
        sleep(50)
    else:
        pin0.write_digital(0)
        pin8.write_digital(0)
        pin1.write_digital(0)
        pin2.write_digital(0)
        display.show(Image.NO)
