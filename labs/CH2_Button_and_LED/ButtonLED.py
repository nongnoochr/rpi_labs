import RPi.GPIO as GPIO

ledPin = 11     
buttonPin = 12

def setup():
    print('Program is starting...')
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)

    # With the circuite provided in the lab, the program still works
    # even without specifying the pull_up_down value becaused we actually
    # create a pull_up_down circuit with
    # 3.3V -> R2 (10k Ohm)  -> GPIO18
    #                       -> Switch

    # However, we are seeing in many gpiozero tutorials we do not need to 
    # create this pull down circuit with rpi and we can directly connect 
    # a switch to a GPIO port and ground. 
    # This is because, internally, if we tell rpi that this GPIO.IN port 
    # is used as -> pull_up_down=GPIO.PUD_UP, rpi will automatically 
    # connect this GPIO port with a VCC (3.3V?) and a resistor which is
    # basically a pull up circuit.
    
    # Hence, directly connect a switch to a GPIO port and a ground will
    # work in this case but we need to ensure that pull_up_down=GPIO.PUD_UP
    # is specified.
    # I tried removing pull_up_down from the setup and it turns out that
    # the LED will always be ON in this case because this IN port will
    # always receive GPIO.LOW in this case regardless of whether the switch
    # is pressed or not (it will always connect to Ground since rpi does not
    # turn on the pull up for you)

    # You will not need to worry about all of this if you are using
    # the Button class of the gpiozero package since the pull_up setting
    # will be used as a default setting but it is at least good to know
    # what it is done behinde the seen :)

    # pull_up_down must be set if switch is directly connect to the port
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # This will also work for the circuit provided in Tutorial.pdf since
    # we also create a pull up circuit outside rpi
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