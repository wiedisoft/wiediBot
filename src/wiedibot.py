from waitress import serve
import cockpit
import configuration as config

'''
This file starts the entire project and load the configuration
'''

# start the bot server
serve(cockpit.app, host=config.host, port=config.port)