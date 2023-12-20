import smtplib, ssl
import os
import dotenv

dotenv.load_dotenv('.env')


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = 'vostic.l24@gmail.com'
    password = os.environ.get('PASS_APP_5')

    receiver = 'vostic.l24@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
