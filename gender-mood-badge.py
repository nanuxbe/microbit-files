from microbit import *

GENDERS = [
    Image('00000:02920:09090:02920:00000'),  # A-gender
    Image('00379:00067:29603:90900:29200'),  # Male
    Image('02720:07070:02720:07770:00700'),  # Female
    Image('00171:00777:27272:70700:27200'),  # Non-binary rotated
    Image('09090:00700:08680:06060:02620'),  # Non-binary
    Image('07970:70907:97979:70907:07970'),  # Intersex
    Image.HEART,
    Image.HAPPY,
    Image.SAD,
    Image.CONFUSED,
    Image.ANGRY,
    Image.ASLEEP,
]

current_index = 0

def change_index(current_index, inc):
    current_index += inc
    if current_index > len(GENDERS) - 1:
        current_index = 0
    if current_index < 0:
        current_index = len(GENDERS) - 1
    return current_index

def next_index(current_index):
    return change_index(current_index, 1)

def previous_index(current_index):
    return change_index(current_index, -1)

while True:
    display.show(GENDERS[current_index])
    if button_a.get_presses() > 0:
        current_index = previous_index(current_index)
    elif button_b.get_presses() > 0:
        current_index = next_index(current_index)