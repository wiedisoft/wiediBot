from waitress import serve
import cockpit
serve(cockpit.app, host='0.0.0.0', port=8080)
