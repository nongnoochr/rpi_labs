import RPi.GPIO as GPIO

ledPin =    11     
buttonPin = 12
ledState =  False

def setup():
    print('Program is starting...')
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)

    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buttonEvent(channel):
    '''
    This function will be triggered when the button is pressed
    '''
    global ledState
    print('buttonEvent GPIO%d' %channel)
    ledState = not ledState

    if ledState:
        print('Turn on LED ...')
    
    else:
        print('Turn off LED ...')
    
    # Update the LED state
    GPIO.output(ledPin, ledState)

def loop():

    # Add an event listener to trigger the buttonEvent callback when the signal is falling
    # with the jitter time interval=300
    GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback=buttonEvent, bouncetime=300)

    # GPIO.add_event_detect(buttonPin, GPIO.RISING, callback=buttonEvent, bouncetime=300)

    while True:
        pass

def destroy():
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':

    setup()

    try:
        loop()
    
    except KeyboardInterrupt:
        destroy()