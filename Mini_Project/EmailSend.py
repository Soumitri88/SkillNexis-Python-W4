#Automate email sending with smtplib.

import smtplib
from email.message import EmailMessage
import os
from getpass import getpass

def send_email(sender, password, receiver, subject, body):
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        # Connect to Gmail's SMTP server
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.send_message(msg)

        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Login failed. Check your email and App Password.")
    except (smtplib.SMTPException, OSError) as error:
        print("Failed to send email:", error)


# Main program
sender = input("Enter your Gmail address: ").strip()
password = getpass("Enter your Gmail App Password: ")
receiver = input("Enter receiver's email address: ").strip()
subject = input("Enter email subject: ")
body = input("Enter your message: ")

send_email(sender, password, receiver, subject, body)
