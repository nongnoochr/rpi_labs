import RPi.GPIO as GPIO
import time
LedPin = 12
def setup():
    global p
    GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by physical location
    GPIO.setup(LedPin, GPIO.OUT) # Set LedPin's mode is output
    GPIO.output(LedPin, GPIO.LOW) # Set LedPin to low
    p = GPIO.PWM(LedPin, 1000) # Set Frequency to 1KHz
    p.start(0) # Duty Cycle = 0
def loop():
    while True:
        for dc in range(0, 101, 1): # Increase duty cycle: 0~100
            p.ChangeDutyCycle(dc) # Change duty cycle
            time.sleep(0.01)
        time.sleep(1)
        for dc in range(100, -1, -1): # Decrease duty cycle: 100~0
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        time.sleep(1)
def destroy():
    p.stop()
    GPIO.output(LedPin, GPIO.LOW) # turn off led
    GPIO.cleanup()

if __name__ == '__main__': # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt: # When 'Ctrl+C' is pressed, the subprogram destroy() will be executed.
        destroy()