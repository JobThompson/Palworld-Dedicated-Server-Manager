from tkinter import messagebox

class Form:
    """Class to handle the form for the GUI."""
    def __init__(self, config) -> None:
        self.config = config

        """Form Labels"""
        self.server_status = None
        self.server_version = None
        self.server_name = None
        self.server_description = None
        self.server_password = None
        self.max_players = None
        self.server_rcon_port = None
        self.server_rcon_enabled = None
        self.server_rcon_password = None
        self.palworld_directory_label = None
        self.arrcon_directory_label = None
        self.steamcmd_directory_label = None
        self.backup_directory_label = None
        
        """Form Entries"""
        self.server_startup_args_entry = None


        
    def open_modal(self, title, message = "This feature is not yet implemented."):
        """Open a modal window with a message."""
        messagebox.showinfo(title, message)

    def select_palworld_directory(self):
        """Open a modal window to select the PalWorld directory."""
        self.open_modal("Select PalWorld Directory")
    
    
    def select_arrcon_directory(self):
        """Open a modal window to select the ARRCON directory."""
        self.open_modal("Select ARRCON Directory")
    
    
    def select_steamcmd_directory(self):
        """Open a modal window to select the SteamCMD directory."""
        self.open_modal("Select SteamCMD Directory")
    
    
    def select_backup_directory(self):
        """Open a modal window to select the backup directory."""
        self.open_modal("Select Backup Directory")