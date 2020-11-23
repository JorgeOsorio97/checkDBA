import requests
from utils import send_email
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
send_email("jorge.valdez.osorio@gmail.com", "CheckDB", BODY_TEXT, BODY_HTML)
# Replace sender@

base_url="http://64acdb529bb1.ngrok.io"

# TODO
# Manda peticion de notificacion al API

# TODO
# Manda informacion del servidor al API para predictor