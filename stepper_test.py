from stepper import *

delay = 3

while True:
    direction = raw_input("The rotation direction (0 is clockwise, 1 is counterclockwise)")
    circles = raw_input("How many circles?")
    if int(direction) == 0:
        print("for")
        forward(int(delay) / 1000.0, int(circles) * 512)
    elif int(direction) == 1:
        print("back")
        backward(int(delay) / 1000.0, int(circles) * 512)
