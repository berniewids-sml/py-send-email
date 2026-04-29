import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os

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
            context = smtplib.ssl.create_default_context()
            server = smtplib.SMTP_SSL(smtp_server, smtp_port, context=context, timeout=10)
        else:
            # TLS connection
            server = smtplib.SMTP(smtp_server, smtp_port, timeout=10)
            server.ehlo()
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
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    # Load configuration from .env file
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "465"))
    SENDER_EMAIL = os.getenv("SENDER_EMAIL")
    SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
    RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
    SUBJECT = os.getenv("EMAIL_SUBJECT", "Test Email")
    BODY = os.getenv("EMAIL_BODY", "This is a test email sent from Python.")
    USE_SSL = os.getenv("USE_SSL", "True").lower() == "true"
    
    # Validate required fields
    if not all([SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL]):
        print("Error: Missing required environment variables. Check your .env file.")
        print("Required: SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL")
    else:
        print(f"Connecting to {SMTP_SERVER}:{SMTP_PORT} (SSL: {USE_SSL})")
        
        send_email(
            smtp_server=SMTP_SERVER,
            smtp_port=SMTP_PORT,
            sender_email=SENDER_EMAIL,
            sender_password=SENDER_PASSWORD,
            receiver_email=RECEIVER_EMAIL,
            subject=SUBJECT,
            body=BODY,
            use_ssl=USE_SSL
        )
