from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

class EmailHandler:
    """Class to handle the email notifications."""
    def __init__(self) -> None:
        pass

    def create_email_message(self, form):
        msg = MIMEMultipart()
        msg['From'] = form.notification_email.get()
        msg['To'] = form.notification_email.get()
        return msg

    def send_email(self, form, msg):
        try:
            server = smtplib.SMTP(form.smtp_server.get(), form.smtp_port.get())
            server.starttls() # Start the TLS encryption
            server.login(form.notification_email.get(), form.notification_email_password.get()) # Login to the email account
            server.sendmail(form.notification_email.get(), form.notification_email.get(), msg) # Send the email
            form.append_to_output(f"Sent notification email successfully to {form.notification_email.get()}.")
        except smtplib.SMTPException:
            pass
        
    def send_crash_email_notification(self, form):
        msg = self.create_email_message(form)
        msg['Subject'] = "Palworld Server Crash"
        msg.attach(MIMEText("This email indicates that the Palworld server was not running. No worries though. The server was restarted.", 'plain'))
        self.send_email(form, msg.as_string())
    
    def send_backup_email_notification(self, form):
        msg = self.create_email_message(form)
        msg['Subject'] = "Palworld Server Backup"
        msg.attach(MIMEText("The server was backed up successfully.", 'plain'))
        self.send_email(form, msg.as_string())