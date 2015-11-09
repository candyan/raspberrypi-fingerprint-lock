import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

enable_pin = 4
coil_A_1_pin = 17
coil_A_2_pin = 18
coil_B_1_pin = 27
coil_B_2_pin = 22

GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

def forward(delay, steps):
    rotate(delay, steps)

def backward(delay, steps):
    rotate(delay, steps, clockwise=False)

def rotate(delay, steps, clockwise=True):
    for step in range(0, steps):
        pins = [0, 0, 0, 0]
        for index in range(0, 4):
            for pin in range(0, 4):
                subscript = (3 - pin) if clockwise else pin
                pins[subscript] = 1 if (pin == index) else 0
            setStep(pins[0], pins[1], pins[2], pins[3])
            time.sleep(delay)


def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)
