from tkinter import messagebox

class Form:
    """Class to handle the form for the GUI."""
    def __init__(self) -> None:
        pass
    
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