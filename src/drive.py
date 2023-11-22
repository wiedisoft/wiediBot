import RPi.GPIO as gpio
import configparser as cp

# Load configuration
config = cp.ConfigParser()
config.read_file(open(r"wiedibot.config"))

# Engine
gpio.setmode(gpio.BCM)

IN1 = (int(config.get("Engine", "IN1")))
IN2 = (int(config.get("Engine", "IN2")))
IN3 = (int(config.get("Engine", "IN3")))
IN4 = (int(config.get("Engine", "IN4")))
ENA = (int(config.get("Engine", "ENA")))
ENB = (int(config.get("Engine", "ENB")))
Hertz = (int(config.get("Engine", "Hertz")))

gpio.setup(ENA, gpio.OUT)
gpio.setup(ENB, gpio.OUT)

leftEngine = {"Channel1":IN3, "Channel2":IN4, "PWM":gpio.PWM(ENB, Hertz)}
rightEngine = {"Channel1":IN1, "Channel2":IN2, "PWM":gpio.PWM(ENA, Hertz)}

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

def CleanUp():
    print("cleaning up")
    gpio.cleanup()

def Forward():
    gpio.output(rightEngine["Channel2"], True)
    gpio.output(leftEngine["Channel2"], True)
    rightEngine["PWM"].ChangeDutyCycle(40)
    leftEngine["PWM"].ChangeDutyCycle(40)

def Backward():
    gpio.output(rightEngine["Channel1"], True)
    gpio.output(leftEngine["Channel1"], True)
    rightEngine["PWM"].ChangeDutyCycle(40)
    leftEngine["PWM"].ChangeDutyCycle(40)

def Left():
    gpio.output(leftEngine["Channel2"], True)
    gpio.output(rightEngine["Channel1"], True)
    leftEngine["PWM"].ChangeDutyCycle(40)  
    rightEngine["PWM"].ChangeDutyCycle(40)

def Right():
    gpio.output(leftEngine["Channel1"], True)
    gpio.output(rightEngine["Channel2"], True)
    leftEngine["PWM"].ChangeDutyCycle(40)  
    rightEngine["PWM"].ChangeDutyCycle(40)

def Stop():
    gpio.output(rightEngine["Channel1"], False)
    gpio.output(rightEngine["Channel2"], False)
    gpio.output(leftEngine["Channel1"], False)
    gpio.output(leftEngine["Channel2"], False)
    rightEngine["PWM"].ChangeDutyCycle(0)
    leftEngine["PWM"].ChangeDutyCycle(0)
