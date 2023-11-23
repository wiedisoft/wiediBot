from flask import Flask, render_template
import signal
import sys
import drive as Drive
import battery
import configuration as config

# starting point of the webserver
app = Flask(__name__, template_folder="templates", static_url_path="/static")

# handle Ctrl+C (SIGINT)
def signal_handler(sig, frame):
    # reset the GPIOs
    Drive.CleanUp()
    sys.exit(0)

# register the signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

# the home path
@app.route('/')
def hello():
    return render_template("index.html")

# get the bot version
@app.route('/GetVersion')
def GetVersion():
    return(config.version)

# get battery charge
@app.route('/GetBattery')
def GetBattery():
    return battery.GetBatteryCharge()

# stop driving
@app.route('/Stop')
def Stop():
    print('Stop')
    Drive.Stop()
    return "Stop"

# drive forward
@app.route('/Forward')
def Forward():
    Drive.Forward()
    return "Driving forward"

# drive left
@app.route('/Left')
def Left():
    Drive.Left()
    print('Left')
    return "Nothing"

# drive right
@app.route('/Right')
def Right():
    Drive.Right()
    print('Right')
    return "Nothing"

# drive backward
@app.route('/Backward')
def Backward():
    print('Backward')
    Drive.Backward()
    return "Nothing"