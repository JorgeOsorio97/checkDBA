
from datetime import datetime as dt
# Manda correo de error

BODY_TEXT = ("ALERTA!!!!!!\r\n"
            "Tu base de datos se ha caido"
            )

BODY_HTML = """<html>
                <head></head>
                <body>
                <h1>ALERTA!!!!!!</h1>
                <p>Tu base de datos se ha caido {}</p>
                </body>
            </html>
            """.format(dt.now())
send_email("jorge.valdez.osorio@gmail.com", "CheckDB", BODY_TEXT, BODY_HTML)
send_sms("Alerta en base de datos {}".format(dt.now()))


