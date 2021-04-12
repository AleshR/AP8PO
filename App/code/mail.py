#!/usr/bin/python3

import smtplib, ssl
import getpass

port = 587
smtp_server = "smtp.gmail.com"

sender_email = "emailovyTester@gmail.com"  # Enter your address
receiver_email = "alesh.ryska@gmail.com"  # Enter receiver address

password = getpass.getpass("Type your password and press enter: ")

message = """\
Subject: Hi there

This message is sent from Python."""

def send_email():
	context = ssl.create_default_context()
	with smtplib.SMTP(smtp_server, port) as server:
		server.ehlo()  # Can be omitted
		server.starttls(context=context)
		server.ehlo()  # Can be omitted
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)
