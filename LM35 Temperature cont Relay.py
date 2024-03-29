# importing the required libraries
from machine import ADC
from machine import Pin
import time

# declare constants
DIODE_OFFSET_VOLTAGE = 0.929  # unit : volt
led_green=Pin(25,Pin.OUT)
led_red=Pin(15,Pin.OUT)

# declaration of pin objects
analogInputPin = ADC(28) # only one positional argument
                          # which is pin id
                          

# main logic of the program
while True:
    # read raw analog signal value
    analogValue = ADC.read_u16(analogInputPin)
    
    # calculate sensor output voltage from raw Analog value
    sensor_voltage = (analogValue / 65535) * 3.3 # unit : Volt
    
    # convert to milli volts
    sensor_voltage = (sensor_voltage - DIODE_OFFSET_VOLTAGE ) * 1000 # unit : milli volt
    
    # calculate temperature from sensor voltage (in millivolt)
    # from datasheet
    # 1 degree celcius = 10 milli volt
        
    temperature = (sensor_voltage/10 ) # unit : degree celcius
        
    time.sleep(1)# sleep is just for demonstration , vary it as per need
        
    print("Temperature = ", temperature, " degree celcius")
    print("\n")
    if temperature <30:
        led_green.on()
    else:
        led_green.off()
    if temperature >31:
        led_red.on()
    else:
        led_red.off()
        