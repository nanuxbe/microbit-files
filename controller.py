import radio
from microbit import button_a, button_b, display, Image, sleep, accelerometer

SPEECH = [
    ("Hello", ),
    ("Name", ),
    ("exterminate", ),
    ("follow", ),
    ("ok", "YES"),
    ("yes", "YES"),
    ("no", "NO"),
    ("understand", "CONFUSED"),
]

INDEX = 0

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


radio.on()
display.scroll(SPEECH[INDEX][0])


def get_direction(method, positive, negative):
    value = (method() + 300) // 700
    if value == 0:
        return None
    value = value // abs(value)
    if value > 0:
        return positive
    return negative

while True:
    ct = button_a.get_presses()
    if ct > 0:
        INDEX += ct
        while INDEX >= len(SPEECH):
            INDEX = INDEX - len(SPEECH)
        display.scroll(SPEECH[INDEX][0])
    if button_b.was_pressed():
        radio.send("say:{}".format(":".join(SPEECH[INDEX])))
        display.show(Image("05750:32023:04640:00000:00900"))
        sleep(250)

    value = None
    for direction in DIRECTIONS:
        value = get_direction(*direction)
        if value is not None:
            break
    if value is None:
        display.show(Image("00000:03730:07970:03730:00000"))
    else:
        display.show(ARROWS[value])
        radio.send("move:{}".format(value))
        sleep(150)
