from tkinter import messagebox, filedialog
import os
from Classes.Function.EmailHandler import EmailHandler
from Classes.Function.DiscordHandler import DiscordHandler
from Classes.Function.ServerHandler import ServerHandler

class Form:
    """Class to handle the form for the GUI."""
    def __init__(self, config) -> None:
        self.config = config
        self.email_handler = EmailHandler()
        self.discord_handler = DiscordHandler()
        self.server_handler = ServerHandler()

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
        self.server_restart_interval = None
        self.daily_restart_time = None
        self.backup_interval = None
        self.monitor_interval = None
        self.send_notification_email = None
        self.send_notification_discord = None
        self.send_backup_notification = None
        self.notification_email = None
        self.notification_email_password = None
        self.smtp_server = None
        self.smtp_port = None
        self.notification_discord_webhook = None

    def import_config(self):
        """imports the configuration settings."""
        self.config.import_config(self)

    def handle_application_close(self):
        """handle the application close event."""
        self.config.export_config(self)

    def open_modal(self, title, message = "This feature is not yet implemented."):
        """Open a modal window with a message."""
        messagebox.showinfo(title, message)


    """Directory Handlers"""
    def select_palworld_directory(self):
        """Open a modal window to select the PalWorld directory."""
        directory_path = filedialog.askdirectory()
        if self.check_for_file("PalWorldServer.exe", directory_path):
            self.palworld_directory_label.configure(text=directory_path)
        else:
            messagebox.showerror("Error", "PalWorldServer.exe not found in the selected directory.")
            self.palworld_directory_label.configure(text="Not Found.", fg_color="red")

    def select_arrcon_directory(self):
        """Open a modal window to select the ARRCON directory."""
        directory_path = filedialog.askdirectory()
        if self.check_for_file("ARRCON.exe", directory_path):
            self.arrcon_directory_label.configure(text=directory_path)
        else:
            messagebox.showerror("Error", "ARRCON.exe not found in the selected directory.")
            self.arrcon_directory_label.configure(text="Not Found.", fg_color="red")

    def select_steamcmd_directory(self):
        """Open a modal window to select the SteamCMD directory."""
        directory_path = filedialog.askdirectory()
        if self.check_for_file("steamcmd.exe", directory_path):
            self.steamcmd_directory_label.configure(text=directory_path)
        else:
            messagebox.showerror("Error", "steamcmd.exe not found in the selected directory.")
            self.steamcmd_directory_label.configure(text="Not Found.", fg_color="red")

    def select_backup_directory(self):
        """Open a modal window to select the backup directory."""
        directory_path = filedialog.askdirectory()
        self.backup_directory_label.configure(text=directory_path)
        
    
    """Utility Functions"""
    def check_for_file(self, target_file_name, directory):
        """Check for a file in a directory."""
        result = [file_name for file_name in os.listdir(directory) if file_name == target_file_name]
        return result