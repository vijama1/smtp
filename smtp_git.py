import smtplib
i=0
sender_email="<sender_mail>"
receiver_email=["<receiver_mail>"]
message = """From: From Person
To: To Person <sender_mail>
Subject: <subject>

<message>:):):):).
"""
username=sender_email
password='<password>'
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
while True:
    server.sendmail(sender_email, receiver_email, message)
server.quit()
