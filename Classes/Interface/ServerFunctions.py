from customtkinter import CTkFrame, CTkButton, CTkLabel, CTkEntry

class ServerFunctions(CTkFrame):
    """Class to handle the server functions widgets."""
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.label_font = ("Arial", 12, "bold")
        
    def create_server_function_widgets(self, form):
        
        start_button = CTkButton(self, text="Start Server", command=lambda: form.server_handler.start_server())
        start_button.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="esw")
        
        restart_button = CTkButton(self, text="Restart Server", command=lambda: form.server_handler.restart_server())
        restart_button.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="esw")
        
        stop_button = CTkButton(self, text="Stop Server", command=lambda: form.server_handler.stop_server())
        stop_button.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="esw")
        
        backup_button = CTkButton(self, text="Backup Server", command=lambda: form.server_handler.backup_server())
        backup_button.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="esw")
        
        update_server_button = CTkButton(self, text="Update Server", command=lambda: form.server_handler.update_server())
        update_server_button.grid(row=5, column=0, padx=10, pady=(10, 0), sticky="esw")
        
        open_server_directory_button = CTkButton(self, text="Open Server Directory", command=lambda: form.server_handler.open_server_directory())
        open_server_directory_button.grid(row=6, column=0, padx=10, pady=(10, 0), sticky="esw")
        
        open_backup_directory_button = CTkButton(self, text="Open Backup Directory", command=lambda: form.server_handler.open_backup_directory())
        open_backup_directory_button.grid(row=7, column=0, padx=10, pady=(10, 0), sticky="esw")