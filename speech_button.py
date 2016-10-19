import speech
from microbit import button_a, button_b, display, Image, sleep

SPEECH = [
    ("Hello", "Hello"),
    ("Name", "My name is Marvin"),
    ("exterminate", "exterminate"),
    ("follow", "Follow me"),
    ("ok", "O K"),
    ("yes", "yes"),
    ("no", "no"),
    ("understand", "I don't understand you. Are you human?"),
]

FACES = [
    Image("00000:09090:00000:99999:00000"),
    Image("00000:09090:03930:09990:03930"),
]

INDEX = 0

display.scroll(SPEECH[INDEX][1])


def speak(to_say):
    global FACES
    words = to_say.split(" ")
    index = 0
    for word in words:
        display.show(FACES[index])
        speech.say(word)
        sleep(10)
        index = 1 - index


while True:
    ct = button_a.get_presses()
    if ct > 0:
        INDEX += ct
        while INDEX >= len(SPEECH):
            INDEX = INDEX - len(SPEECH)
        display.scroll(SPEECH[INDEX][0])
    if button_b.was_pressed():
        speak(SPEECH[INDEX][1])
    display.show(Image.HAPPY)