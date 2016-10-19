from microbit import *


ct = 0
direction = 1

# pin0.write_digital(1)

top = 1110
side = 11111

while True:
    sleep(100)
    # display.scroll(str(pin0.read_analog()))
    val = max((pin0.read_analog() - 843) // 20, 0)
    
    matrix = "{top}:{side}:{side}:{side}:{top}".format(
        top="{:05d}".format(top * val),
        side="{:05d}".format(side * val)
    )
    
    display.show(Image(matrix))

#    if ct <= 0:
#        direction = 1
#    elif ct >= 1023:
#        direction = -1
    
#    if ct // 128 == ct / 128:
#        display.scroll(str(ct))
    
#     ct += direction
#     pin0.write_analog(ct)