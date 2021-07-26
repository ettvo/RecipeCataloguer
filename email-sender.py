import smtplib, ssl
# (SSL) is a networking protocol designed for securing connections between web clients and web servers over an insecure network
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "recipesforbrokecollegekids@gmail.com"  # Enter your address
receiver_email = "karynpham@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ") #PW: @GoBears101
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)