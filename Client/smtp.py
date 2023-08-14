import smtplib
from email.message import EmailMessage

def send_email(sender_email, sender_password, receiver_email, subject, body):
    try:
        # Set up the SMTP server and login to your email account
        
        # Create the email message
        message = EmailMessage()
        message.set_content(body)
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        
        smtp_server = 'smtp.gmail.com'  # Replace with your SMTP server (e.g., smtp.example.com for other providers)
        smtp_port = 587  # Replace with the appropriate SMTP port (587 for TLS)
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.send_message(message)

        # Close the connection
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print("An error occurred while sending the email:", str(e))

# Example usage
if __name__ == "__main__":
    sender_email = 'swamayyappa197@gmial.com'  # Replace with your email address
    sender_password = 'phnghgkhypyoikba'  # Replace with your email password
    receiver_email = '20b81a3368@cvr.ac.in'  # Replace with the recipient's email address
    subject = 'Test Email'
    body = 'This is a test email sent using Python.'

    send_email(sender_email, sender_password, receiver_email, subject, body)
