import speech
import radio
from microbit import display, Image, sleep

FACES = [
    Image("00000:09090:00000:99999:00000"),
    Image("00000:09090:03930:09990:03930"),
]

NAMED_FACES = {
    "HAPPY": Image.HAPPY,
    "YES": Image.YES,
    "NO": Image.NO,
    "CONFUSED": Image.CONFUSED,
}

SPEECH = {
    "Hello": "Hello",
    "Name": "My name is Marvin",
    "exterminate": "exterminate",
    "follow": "Follow me",
    "ok": "O K",
    "yes": "yes",
    "no": "no",
    "understand": "I don't understand you. Are you human?",
}


def speak(to_say, face=None):
    global FACES, NAMED_FACES, SPEECH
    index = 0
    if to_say in SPEECH:
        words = SPEECH[to_say].split(" ")
        for word in words:
            display.show(FACES[index])
            speech.say(word)
            sleep(10)
            index = 1 - index
    if face is not None and face in NAMED_FACES:
        display.show(NAMED_FACES[face])
        sleep(1000)


radio.on()

while True:
    try:
        message = radio.receive()
    except ValueError:
        radio.off()
        sleep(100)
        radio.on()
        message = None

    if message is not None:
        data = message.split(":")
        if data[0] == "say":
            speak(data[1], data[2] if len(data) > 2 else None)
    display.show(Image.HAPPY)
