import requests
import json
from datetime import datetime as dt
from utils import send_email, send_sms
# Manda correo de error

BODY_TEXT = ("ALERTA!!!!!!\r\n"
            "Tu base de datos se ha caido"
            )

BODY_HTML = """<html>
                <head></head>
                <body>
                <h1>ALERTA!!!!!!</h1>
                <p>Tu base de datos se ha caido</p>
                </body>
            </html>
            """
# send_email("jorge.valdez.osorio@gmail.com", "CheckDB", BODY_TEXT, BODY_HTML)
# send_sms("Alerta en base de datos")

base_url="http://64acdb529bb1.ngrok.io"

# TODO
# Manda peticion de notificacion al API
payload = {
    "status": "todo bien",
    "date": str(dt.now())
}
headers = {
  'Content-Type': 'application/json'
}
response = requests.request("POST", base_url + "/status", headers=headers, data=json.dumps(payload))
print(response)

# TODO
# Manda informacion del servidor al API para predictor