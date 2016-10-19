from microbit import *
import random

dices = [
    Image('00000:00000:00500:00000:00000'),
    Image('05000:00000:00000:00000:00050'),
    Image('05000:00000:00500:00000:00050'),
    Image('05050:00000:00000:00000:05050'),
    Image('05050:00000:00500:00000:05050'),
    Image('05050:00000:05050:00000:05050'),
]

numbers = [
    Image('05550:05050:05050:05050:05550'),
    Image('00500:05500:00500:00500:05550'),
    Image('05550:00050:05550:05000:05550'),
    Image('05550:00050:05550:00050:05550'),
    Image('05050:05050:05550:00050:00050'),
    Image('05550:05000:05550:00050:05550'),
    Image('05550:05000:05550:05050:05550'),
    Image('05550:00050:00050:00050:00050'),
    Image('05550:05050:05550:05050:05550'),
    Image('05550:05050:05550:00050:05550'),
]

animals = [
    Image('07700:77700:07777:07770:00000'),
    Image('77000:07000:07000:07770:07070'),
    Image('70700:70700:77770:77070:77770'),
    Image('70007:70007:77777:07770:00700'),
    Image('77000:77077:07070:07770:00000'),
]

surprise = [
    Image('77777:00700:00700:00700:77777'),
    Image('70000:70000:70000:70000:77777'),
    Image('77777:70007:70007:70007:77777'),
    Image('00000:00000:70007:07070:00700'),
    Image('77777:70000:77777:70000:77777'),
    Image('70007:07070:00700:00700:00700'),
    Image('77777:70007:70007:70007:77777'),
    Image('70007:70007:70007:70007:77777'),
    Image('07070:77777:77777:07770:00700'),
]

python = [
    Image('77777:00700:00700:00700:77777'),
    Image('70000:70000:70000:70000:77777'),
    Image('77777:70007:70007:70007:77777'),
    Image('00000:00000:70007:07070:00700'),
    Image('07770:07070:07770:07000:07000'),
]


# display.show(python[4])

# while True:
#     gesture = accelerometer.current_gesture()
#     if gesture == "face up":
#         display.show(Image.HAPPY)
#     elif gesture == "shake":
#         display.show(Image.CHESSBOARD)
#     else:
#         display.show(Image.ANGRY)

while True:
    
    # gesture = accelerometer.current_gesture()
    # if button_a.get_presses() > 0:
    if accelerometer.was_gesture("shake") or button_a.get_presses() > 0:
        # display.scroll(accelerometer.current_gesture())
        my_dices = []
        for i in range(3):
            my_dices.append(random.choice(dices))
        display.show(my_dices)
            # sleep(50)
    # else:
    #     sleep(100)