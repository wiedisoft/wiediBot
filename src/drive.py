import RPi.GPIO as gpio
import configuration as config

# Engine
gpio.setmode(gpio.BCM)
gpio.setup(config.ENA, gpio.OUT)
gpio.setup(config.ENB, gpio.OUT)

leftEngine = {"Channel1":config.IN3, "Channel2":config.IN4, "PWM":gpio.PWM(config.ENB, config.Hertz)}
rightEngine = {"Channel1":config.IN1, "Channel2":config.IN2, "PWM":gpio.PWM(config.ENA, config.Hertz)}

DC_MAX = 70

gpio.setup(rightEngine["Channel1"], gpio.OUT)
gpio.setup(rightEngine["Channel2"], gpio.OUT)
gpio.setup(leftEngine["Channel1"], gpio.OUT)
gpio.setup(leftEngine["Channel2"], gpio.OUT)

gpio.output(rightEngine["Channel1"], False)
gpio.output(rightEngine["Channel2"], False)
gpio.output(leftEngine["Channel1"], False)
gpio.output(leftEngine["Channel2"], False)

rightEngine["PWM"].start(0)
rightEngine["PWM"].ChangeDutyCycle(0)

leftEngine["PWM"].start(0)
leftEngine["PWM"].ChangeDutyCycle(0)

# cleaning up the gpio
def CleanUp():
    gpio.cleanup()

# drive forward
def Forward():
    gpio.output(rightEngine["Channel2"], True)
    gpio.output(leftEngine["Channel2"], True)
    rightEngine["PWM"].ChangeDutyCycle(40)
    leftEngine["PWM"].ChangeDutyCycle(40)

# drive backward
def Backward():
    gpio.output(rightEngine["Channel1"], True)
    gpio.output(leftEngine["Channel1"], True)
    rightEngine["PWM"].ChangeDutyCycle(40)
    leftEngine["PWM"].ChangeDutyCycle(40)

# drive left
def Left():
    gpio.output(leftEngine["Channel2"], True)
    gpio.output(rightEngine["Channel1"], True)
    leftEngine["PWM"].ChangeDutyCycle(40)  
    rightEngine["PWM"].ChangeDutyCycle(40)

#drive right
def Right():
    gpio.output(leftEngine["Channel1"], True)
    gpio.output(rightEngine["Channel2"], True)
    leftEngine["PWM"].ChangeDutyCycle(40)  
    rightEngine["PWM"].ChangeDutyCycle(40)

# brake
def Stop():
    gpio.output(rightEngine["Channel1"], False)
    gpio.output(rightEngine["Channel2"], False)
    gpio.output(leftEngine["Channel1"], False)
    gpio.output(leftEngine["Channel2"], False)
    rightEngine["PWM"].ChangeDutyCycle(0)
    leftEngine["PWM"].ChangeDutyCycle(0)
