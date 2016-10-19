import radio
from microbit import button_a, button_b, display, Image, sleep, accelerometer

DIRECTIONS = [
    (accelerometer.get_y, "backwards", "forwards"),
    (accelerometer.get_x, "right", "left"),
]

ARROWS = {
    "backwards": Image.ARROW_S,
    "forwards": Image.ARROW_N,
    "left": Image.ARROW_W,
    "right": Image.ARROW_E,
}

SLEEP_TIME = 150


def get_direction(method, positive, negative):
    value = (method() + 300) // 700
    if value == 0:
        return None
    value = value // abs(value)
    if value > 0:
        return positive
    return negative


radio.on()


while True:
    rv = None
    ct_a = button_a.get_presses()
    if ct_a > 0:
        rv = 'btn:a'
    else:
        ct_b = button_b.get_presses()
        if ct_b > 0:
            rv = 'btn:b'
    if rv is not None:
        print(rv)
        radio.send(rv)
        sleep(SLEEP_TIME)

    value = None
    for direction in DIRECTIONS:
        value = get_direction(*direction)
        if value is not None:
            break
    if value is None:
        display.show(Image("00000:03730:07970:03730:00000"))
    else:
        display.show(ARROWS[value])
        rv = "move:{}".format(value)
        print(rv)
        radio.send(rv)
        sleep(SLEEP_TIME)
