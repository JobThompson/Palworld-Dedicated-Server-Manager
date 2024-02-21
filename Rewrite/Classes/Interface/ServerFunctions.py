from customtkinter import CTkFrame, CTkButton, CTkLabel, CTkEntry

class ServerFunctions(CTkFrame):
    """Class to handle the server functions widgets."""
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.grid(row=0, column=2, columnspan=1, rowspan=2, padx=20, pady=10, sticky="ne")
        self.label_font = ("Arial", 12, "bold")
        
    def create_server_function_widgets(self, form):
        restart_button = CTkButton(self, text="Restart Server", command=lambda: form.restart_server())
        restart_button.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="esw")
        
        stop_button = CTkButton(self, text="Stop Server", command=lambda: form.stop_server())
        stop_button.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="esw")
        
        start_button = CTkButton(self, text="Start Server", command=lambda: form.start_server())
        start_button.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="esw")
        
        backup_button = CTkButton(self, text="Backup Server", command=lambda: form.backup_server())
        backup_button.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="esw")
        
        delete_backups_button = CTkButton(self, text="Delete Old Backups", command=lambda: form.delete_old_backups())
        delete_backups_button.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="esw")
        
        update_server_button = CTkButton(self, text="Update Server", command=lambda: form.update_server())
        update_server_button.grid(row=5, column=0, padx=10, pady=(10, 0), sticky="esw")
        
        send_email_button = CTkButton(self, text="Send Email", command=lambda: form.send_email())
        send_email_button.grid(row=6, column=0, padx=10, pady=(10, 0), sticky="esw")
        
        send_discord_button = CTkButton(self, text="Send Discord Message", command=lambda: form.send_discord_message())
        send_discord_button.grid(row=7, column=0, padx=10, pady=(10, 0), sticky="esw")
        
        open_server_directory_button = CTkButton(self, text="Open Server Directory", command=lambda: form.open_server_directory())
        open_server_directory_button.grid(row=8, column=0, padx=10, pady=(10, 0), sticky="esw")
        
        open_backup_directory_button = CTkButton(self, text="Open Backup Directory", command=lambda: form.open_backup_directory())
        open_backup_directory_button.grid(row=9, column=0, padx=10, pady=(10, 0), sticky="esw")