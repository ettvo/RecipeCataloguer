from datetime import date
import smtplib, ssl
import calendar

weekday = calendar.day_name[date.today().weekday()]
name = "Karyn"


# (SSL) is a networking protocol designed for securing connections between web clients and web servers over an insecure network
port = 465  # For SMTP over SSL
smtp_server = "smtp.gmail.com" #SMTP server address: The socket(?) between gmail.com (587) and SMTP (465)
sender_email = "recipesforbrokecollegekids@gmail.com"  # Recipe email Address
receiver_email = "karynpham@gmail.com"  # Test recipient: Me!
password = input("Type your password and press enter: ") #PW: @GoBears101
message = """\
Subject: Here's Your {weekday} Recipe {name}!

This message is sent from Python.""".format(weekday=weekday, name = name)
# Text after "Subject: " will automatically be placed in the subject line of the email
context = ssl.create_default_context() #Provides TLS access on client and server side
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server: #smtplib is a SMTP instance that haa methods supporting SMTP
    server.login(sender_email, password) #logs into sender_email on gmail.com
    server.sendmail(sender_email, receiver_email, message) #sends a simple message to receiver with a subject line and plain text