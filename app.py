import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def send_email(smtp_server, smtp_port, sender_email, sender_password, receiver_email, subject, body, use_ssl=True):
    """
    Send email using SMTP server
    
    Args:
        smtp_server: SMTP server address (e.g., 'smtp.gmail.com')
        smtp_port: SMTP port (587 for TLS, 465 for SSL)
        sender_email: Sender's email address
        sender_password: Sender's email password or app password
        receiver_email: Receiver's email address
        subject: Email subject
        body: Email body text
        use_ssl: Use SSL (True) or TLS (False)
    """
    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = Header(subject, 'utf-8')
    
    # Add body
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    
    try:
        if use_ssl:
            # SSL connection
            server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        else:
            # TLS connection
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
        
        # Login
        server.login(sender_email, sender_password)
        
        # Send email
        server.send_message(msg)
        server.quit()
        
        print("Email sent successfully!")
        return True
    
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False


if __name__ == "__main__":
    # Example usage - configure these settings
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 465  # Use 587 for TLS
    SENDER_EMAIL = "your_email@gmail.com"
    SENDER_PASSWORD = "your_app_password"
    RECEIVER_EMAIL = "recipient@example.com"
    SUBJECT = "Test Email"
    BODY = "This is a test email sent from Python."
    
    send_email(
        smtp_server=SMTP_SERVER,
        smtp_port=SMTP_PORT,
        sender_email=SENDER_EMAIL,
        sender_password=SENDER_PASSWORD,
        receiver_email=RECEIVER_EMAIL,
        subject=SUBJECT,
        body=BODY,
        use_ssl=True
    )
