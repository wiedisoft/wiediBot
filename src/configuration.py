import configparser as cp

# load the configuration
config = cp.ConfigParser()
config.read_file(open(r"wiedibot.config"))

# bot version
version = "0.1.0.2"

# get configurtion values
host = (config.get("Server", "Host"))
port = (config.get("Server", "Port"))

# configurations for the engines
IN1 = (int(config.get("Engine", "IN1")))
IN2 = (int(config.get("Engine", "IN2")))
IN3 = (int(config.get("Engine", "IN3")))
IN4 = (int(config.get("Engine", "IN4")))
ENA = (int(config.get("Engine", "ENA")))
ENB = (int(config.get("Engine", "ENB")))
Hertz = (int(config.get("Engine", "Hertz")))