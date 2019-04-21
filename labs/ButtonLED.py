import RPi.GPIO as GPIO

ledPin = 11     
buttonPin = 12

def setup():
    print('Program is starting...')
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # GPIO.setup(buttonPin, GPIO.IN)

def loop():
    while True:
        if GPIO.input(buttonPin) == GPIO.LOW:
           GPIO.output(ledPin, GPIO.HIGH) 
           print('led on....')
        
        else:
            GPIO.output(ledPin, GPIO.LOW)
            print('led off...')

def destroy():
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    print('Hello WOLRD!')

    setup()
    try:
        loop()
    
    except KeyboardInterrupt:
        destroy()