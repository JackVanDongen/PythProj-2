# The following code is copied from: https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/ 
# The program flashes a LED using the GPIO.PWM fonction 

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 0.5)
p.start(1)
input('Press return to stop:')   # use raw_input for Python 2
p.stop()
GPIO.cleanup()