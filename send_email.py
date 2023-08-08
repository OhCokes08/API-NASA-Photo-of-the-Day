import smtplib
import ssl

def sendEmail(message):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()
    username = "femiecoker@gmail.com"
    password = "hsnmukrbfzicdraz"
    receiver = "femiecoker@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)