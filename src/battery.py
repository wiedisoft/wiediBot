import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Initialize the I2C interface
i2c = busio.I2C(board.SCL, board.SDA)
 
# Create an ADS1115 object
ads = ADS.ADS1115(i2c)
 
# Define the analog input channels
channel0 = AnalogIn(ads, ADS.P0)

def GetBatteryCharge():
    # get value of channel0 as float
    value = float("{:.1f}".format(channel0.voltage * 5.59))
    
    # calculate the value in percent
    mapped_value = round(((value - 8.6) / (12.3 - 8.6)) * (100))
    return str(mapped_value)