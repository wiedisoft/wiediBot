from flask import Flask, render_template
import signal
import sys
import drive as Drive
import battery

app = Flask(__name__, template_folder="templates", static_url_path="/static")


# Define a function to handle Ctrl+C (SIGINT)
def signal_handler(sig, frame):
    Drive.CleanUp()
    # Perform cleanup actions here if necessary
    sys.exit(0)

# Register the signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/GetBattery')
def GetBattery():
    return battery.GetBatteryCharge()

@app.route('/Stop')
def Stop():
    print('Stop')
    Drive.Stop()
    return "Stop"

@app.route('/Forward')
def Forward():
    Drive.Forward()
    return "Driving forward"

@app.route('/Left')
def Left():
    Drive.Left()
    print('Left')
    return "Nothing"

@app.route('/Right')
def Right():
    Drive.Right()
    print('Right')
    return "Nothing"

@app.route('/Backward')
def Backward():
    print('Backward')
    Drive.Backward()
    return "Nothing"