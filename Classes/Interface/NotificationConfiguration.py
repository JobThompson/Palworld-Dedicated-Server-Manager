from customtkinter import CTkFrame, BooleanVar, CTkCheckBox

class NotificationConfiguration(CTkFrame):
    """Class to handle the notification configuration widgets."""
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.label_font = ("Arial", 12, "bold")
        
    def create_notification_configuration(self, form):
        form.send_notification_email = BooleanVar()
        send_notification_email_checkbox_var = CTkCheckBox(self, text="Send Notifications", font=self.label_font, variable=form.send_notification_email)
        send_notification_email_checkbox_var.grid(row=0, column=0, padx=20, pady=(0,10), sticky="w")
        
        form.send_notification_discord = BooleanVar()
        send_notification_discord_checkbox_var = CTkCheckBox(self, text="Send Notifications to Discord", font=self.label_font, variable=form.send_notification_discord)
        send_notification_discord_checkbox_var.grid(row=1, column=0, padx=20, pady=(0,10), sticky="w")
        
        form.send_backup_notification = BooleanVar()
        send_backup_notification_checkbox_var = CTkCheckBox(self, text="Send Backup Notifications", font=self.label_font, variable=form.send_backup_notification)
        send_backup_notification_checkbox_var.grid(row=2, column=0, padx=20, pady=(0,10), sticky="w")
        
