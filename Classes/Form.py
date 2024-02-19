from datetime import datetime
from tkinter import filedialog, messagebox
import os, subprocess

class Form:
    """Class to handle inputs in the interface form."""
    def __init__(self):
        self.restart_entry = None
        self.restart_schedule_entry = None
        self.ampm_var = None
        self.monitor_interval_checkbox_var = None
        self.monitor_entry = None
        self.enable_backups_checkbox_var = None
        self.backup_interval_checkbox_var = None
        self.backup_interval_entry = None
        self.send_email_checkbox_var = None
        self.discord_webhook_checkbox_var = None
        self.update_server_startup_checkbox_var = None
        self.backup_server_checkbox_var = None
        self.delete_old_backups_checkbox_var = None
        self.delete_old_backups_entry = None
        self.server_directory_selection = None
        self.server_start_args_entry = None
        self.email_address_entry = None
        self.email_password_entry = None
        self.smtp_server_entry = None
        self.discord_entry = None
        self.arrcon_directory_selection = None
        self.steamcmd_directory_selection = None
        self.backup_directory_selection = None

        """Server Settings"""
        self.rcon_port = None
        self.rcon_state = None
        self.rcon_password = None
        self.max_players = None
        self.server_name = None
        self.server_description = None
        self.server_password = None
        self.server_port = None
        
        """Labels"""
        self.palworld_exe_result_label = None
        self.arrcon_exe_result_label = None
        self.steamcmd_exe_result_label = None
        
        """Output Console"""
        self.output_text = None


    def append_to_output(self, message):
        """Function that sends message to output window"""
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        formatted_message = timestamp + message
        self.output_text.insert("end", formatted_message + "\n")
        self.output_text.yview("end")  # Auto-scroll to the bottom


    def open_modal(self, title, message):
        """Open a modal window with a message."""
        messagebox.showinfo(title, message)


    def get_directory(self):
        """Open a file dialog."""
        return filedialog.askdirectory()


    def open_ini_file(self, directory):
        """Open the PalWorldSettings.ini file in the selected directory."""
        if not directory == "No directory selected":
            ini_file_path = os.path.join(directory, 'Pal', 'Saved', 'Config', 'WindowsServer', 'PalWorldSettings.ini')
            if os.path.isfile(ini_file_path):
                try:
                    subprocess.Popen(['start', '', ini_file_path], shell=True)
                except OSError as e:
                    self.append_to_output("Error opening file: " + str(e))
            else:
                self.append_to_output("You need to select a valid directory first.")
                self.open_modal("Invalid Directory", "You need to select a valid directory first")
        else:
            self.append_to_output("You need to select a valid directory first.")
            self.open_modal("Invalid Directory", "You need to select a valid directory first")


form = Form()
