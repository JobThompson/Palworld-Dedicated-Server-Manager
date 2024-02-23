from customtkinter import CTkFrame, CTkButton, CTkLabel, CTkEntry

class ServerConfiguration(CTkFrame):
    """Class to handle the server configuration widgets."""
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.label_font = ("Arial", 12, "bold")
        
    def create_server_configuration(self, form) -> None:
        """Create the server configuration widgets."""
        # Column 0
        select_palworld_directory_button = CTkButton(self, text="Select PalWorld Directory", command=lambda: form.select_palworld_directory())
        select_palworld_directory_button.grid(row=0, column=0, columnspan=1, padx=10, pady=(10, 0), sticky="esw")
        
        select_arrcon_directory_button = CTkButton(self, text="Select ARRCON Directory", command=lambda: form.select_arrcon_directory())
        select_arrcon_directory_button.grid(row=1, column=0, columnspan=1, padx=10, pady=(10, 0), sticky="esw")
        
        select_steamcmd_directory_button = CTkButton(self, text="Select SteamCMD Directory", command=lambda: form.select_steamcmd_directory())
        select_steamcmd_directory_button.grid(row=2, column=0, columnspan=1, padx=10, pady=(10, 0), sticky="esw")
        
        select_backup_directory_button = CTkButton(self, text="Select Backup Directory", command=lambda: form.select_backup_directory())
        select_backup_directory_button.grid(row=3, column=0, columnspan=1, padx=10, pady=(10, 0), sticky="esw")
        
        
        # Column 1
        form.palworld_directory_label = CTkLabel(self, text="palworld_directory", fg_color="transparent")
        form.palworld_directory_label.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="w")
        
        form.arrcon_directory_label = CTkLabel(self, text="arrcon_directory", fg_color="transparent")
        form.arrcon_directory_label.grid(row=1, column=1,  padx=10, pady=(10, 0), sticky="w")
        
        form.steamcmd_directory_label = CTkLabel(self, text="steamcmd_directory", fg_color="transparent")
        form.steamcmd_directory_label.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="w")
        
        form.backup_directory_label = CTkLabel(self, text="backup_directory", fg_color="transparent")
        form.backup_directory_label.grid(row=3, column=1, padx=10, pady=(10, 0), sticky="w")
        
        
        # Bottom Row
        server_startup_args_label = CTkLabel(self, text="Server Startup Args:", fg_color="transparent", font=self.label_font)
        server_startup_args_label.grid(row=4, column=0, columnspan=1, padx=10, pady=(10, 0), sticky="sw")
        
        form.server_startup_args_entry = CTkEntry(self, width=300)
        form.server_startup_args_entry.grid(row=4, column=1, columnspan=4, padx=10, pady=(10, 0), sticky="esw")
        