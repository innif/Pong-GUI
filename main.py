from display import Display
import time

d = Display()

# Field is shaped 800x600
# Pads have the shape 20x100
# Ball has the shape 20x20
# Positions are always Center Values
# Center of the Pads is 20px away from the border

while True:
    if d.isDownPressed():
        d.movePadRight(1)
    if d.isUpPressed():
        d.movePadLeft(-1)
    time.sleep(0.01)
    d.update()