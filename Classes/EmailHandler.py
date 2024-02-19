import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Classes.Form import form

class EmailHandler:
    """Class that handles the email alerts for the server"""
    def __init__(self) -> None:
        self.smtp_server = None
        self.smtp_port = None
        self.smtp_user = None
        self.smtp_password = None
    
    
    def create_email(self, to_email, subject = "Palworld Server Crash", body = "This email indicates that the Palworld server was not running. No worries though. The server was restarted. Beep beep boop."):
        """Create an email with the given subject and body"""
        msg = MIMEMultipart()
        msg['From'] = self.smtp_user
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        return msg.as_string()
    
    
    def send_email(self, email_to, msg):
        """Send the email to the given email address"""
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls() # Start the TLS encryption
            server.login(self.smtp_user, self.smtp_password) # Login to the email account
            server.sendmail(self.smtp_user, email_to, msg) # Send the email
            form.append_to_output("Sent notification email successfully.")

        except smtplib.SMTPException:
            pass
        
email_handler = EmailHandler()