from customtkinter import CTkFrame, BooleanVar, CTkCheckBox, CTkEntry, CTkLabel

class NotificationConfiguration(CTkFrame):
    """Class to handle the notification configuration widgets."""
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.label_font = ("Arial", 12, "bold")
        
    def create_notification_configuration(self, form):
        # Column 0
        form.send_notification_email = BooleanVar()
        send_notification_email_checkbox_var = CTkCheckBox(self, text="Send Notifications", font=self.label_font, variable=form.send_notification_email)
        send_notification_email_checkbox_var.grid(row=0, column=0, padx=20, pady=(0,10), sticky="w")
        
        form.send_notification_discord = BooleanVar()
        send_notification_discord_checkbox_var = CTkCheckBox(self, text="Send Notifications to Discord", font=self.label_font, variable=form.send_notification_discord)
        send_notification_discord_checkbox_var.grid(row=1, column=0, padx=20, pady=(0,10), sticky="w")
        
        form.send_backup_notification = BooleanVar()
        send_backup_notification_checkbox_var = CTkCheckBox(self, text="Send Backup Notifications", font=self.label_font, variable=form.send_backup_notification)
        send_backup_notification_checkbox_var.grid(row=2, column=0, padx=20, pady=(0,10), sticky="w")
        
        # Column 1
        notification_email_label = CTkLabel(self, text="Notification Email:", fg_color="transparent", font=self.label_font)
        notification_email_label.grid(row=0, column=1, padx=10, pady=(0,10), sticky="w")
        
        notification_email_password_label = CTkLabel(self, text="Notification Email Password:", fg_color="transparent", font=self.label_font)
        notification_email_password_label.grid(row=1, column=1, padx=10, pady=(0,10), sticky="w")
        
        smtp_server_label = CTkLabel(self, text="SMTP Server:", fg_color="transparent", font=self.label_font)
        smtp_server_label.grid(row=2, column=1, padx=10, pady=(0,10), sticky="w")
        
        smtp_port_label = CTkLabel(self, text="SMTP Port:", fg_color="transparent", font=self.label_font)
        smtp_port_label.grid(row=3, column=1, padx=10, pady=(0,10), sticky="w")
        
        notification_discord_webhook_label = CTkLabel(self, text="Discord Webhook:", fg_color="transparent", font=self.label_font)
        notification_discord_webhook_label.grid(row=4, column=1, padx=10, pady=(0,10), sticky="w")
        

        # Column 2
        form.notification_email = CTkEntry(self, width=120)
        form.notification_email.grid(row=0, column=2, padx=10, pady=(0,10), sticky="w")
        
        form.notification_email_password = CTkEntry(self, width=120)
        form.notification_email_password.grid(row=1, column=2, padx=10, pady=(0,10), sticky="w")
        
        form.smtp_server = CTkEntry(self, width=120)
        form.smtp_server.grid(row=2, column=2, padx=10, pady=(0,10), sticky="w")
        
        form.smtp_port = CTkEntry(self, width=120)
        form.smtp_port.grid(row=3, column=2, padx=10, pady=(0,10), sticky="w")
        
        form.notification_discord_webhook = CTkEntry(self, width=120)
        form.notification_discord_webhook.grid(row=4, column=2, padx=10, pady=(0,10), sticky="w")