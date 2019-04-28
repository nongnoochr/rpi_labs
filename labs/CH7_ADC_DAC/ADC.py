import smbus
import time

from tkinter import *

# Default address of PCF8591
address = 0x48 

bus = smbus.SMBus(1)
cmd = 0x40

root = Tk()
my_value = Label(root, text='Hello World')
my_value.grid(row=0, column=0,sticky="sw")

my_voltage = Label(root, text='Hello World')
my_voltage.grid(row=1, column=0,sticky="sw")

def analogRead(chn):
    # Read ADC value, chn: 0, 1, 2, 3
    value = bus.read_byte_data(address, cmd+chn)
    return value

def analogWrite(value):
    # write DAC value
    bus.write_byte_data(address, cmd, value)

def loop():
    while True:
        READ()
        time.sleep(0.01)

def READ():
    value = analogRead(0)   #read the ADC value of channel 0
    analogWrite(value)      # write the DAC value
    voltage = value / 255.0 * 3.3   # calculate the voltage value
    print('ADC Value: %d, Voltag  e: %.2f' %(value, voltage) )
    return (value, voltage)
    

def read_continuosly():
    # Get the current Digital and voltage values
    (value, voltage) = READ()

    # Update text in the app
    my_value.configure(text= "Current Value: {value:3d}".format( value=value))
    my_voltage.configure(text= "Current Voltage: {value:6.2f}".format( value=voltage))
    
    # Keep doing this every 100 ms
    root.after(100, read_continuosly)
    

def destroy():
    bus.close()

def launchApp():
    
    read_continuosly()
    root.mainloop()

if __name__ == '__main__':
    print('Program is starting ... ')
    try:
        launchApp()
        # loop()
    except KeyboardInterrupt:
        destroy()
        