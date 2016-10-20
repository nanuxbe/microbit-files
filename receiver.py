import radio
from microbit import display, Image, sleep


RECEIVE = Image("05750:32023:04640:00000:00900")
DOT = Image("00000:00000:00600:00000:00000")

radio.on()
display.show(DOT)

while True:
    try:
        message = radio.receive()
    except ValueError:
        radio.off()
        sleep(100)
        radio.on()
        message = None

    if message is not None:
        display.show(RECEIVE)
        print(message)
        sleep(50)
    else:
        display.show(DOT)
