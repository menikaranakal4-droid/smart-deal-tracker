import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


def send_price_alert(product):
    sender_email = os.getenv("EMAIL_ADDRESS")
    sender_password = os.getenv("EMAIL_PASSWORD")

    message = EmailMessage()

    message["Subject"] = f"Price Alert - {product['name']}"
    message["From"] = sender_email
    message["To"] = product["email"]

    message.set_content(
        f"""Good news!

{product['name']} has reached your target price.

Target price: {product['target_price']}
Current price: {product.get('current_price')}
"""
    )

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(sender_email, sender_password)
        connection.send_message(message)