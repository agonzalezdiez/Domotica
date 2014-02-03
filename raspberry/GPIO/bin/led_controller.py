import sys
import RPi.GPIO as GPIO


value = sys.argv[1]

if value == '1' or value == '0':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    

    GPIO.output(7, False if value=='0' else True)
