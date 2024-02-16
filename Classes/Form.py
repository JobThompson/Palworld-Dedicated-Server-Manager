from datetime import datetime
from tkinter import filedialog, messagebox
import subprocess
import os
import re

class Form:
    """Class to handle inputs in the interface form."""
    def __init__(self):
        self.restart_entry = None
        self.restart_schedule_entry = None
        self.ampm_var = None
        self.monitor_interval_checkbox_var = None
        self.monitor_entry = None
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


    def select_palworld_directory(self):
        """Open a file dialog to select the PalWorld directory."""
        directory_path = filedialog.askdirectory()
        if directory_path:
            self.server_directory_selection.config(text=f"{directory_path}", foreground="black")
            self.search_file(directory_path, "PalServer.exe")
            # get_server_info(directory_path)
        else:
            self.server_directory_selection.config(text="No directory selected", foreground="red")
            self.palworld_exe_result_label.config(text="PalServer.exe not found", foreground="red")
            self.append_to_output("The directory you selected does not contain the PalServer.exe and other file information required to run this application. Please verify the directory")
        messagebox.showinfo("Invalid Directory", "PalServer.exe was not found in the selected directory")


    def search_file(self, directory, target_file):
        """Search for a file in the selected directory."""
        if target_file == "PalServer.exe":
            if not directory == "No directory selected":
                files_in_directory = os.listdir(directory)
                if target_file in files_in_directory:
                    self.palworld_exe_result_label.config(text=f"{target_file} detected", foreground="green")
                else:
                    self.palworld_exe_result_label.config(text=f"{target_file} not found", foreground="red")
                    messagebox.showinfo("Invalid Directory", "PalServer.exe was not found in the selected directory")
            else:
                self.palworld_exe_result_label.config(text=f"{target_file} not found", foreground="red")
        elif target_file == "ARRCON.exe":
            if not directory == "No directory selected":
                files_in_directory = os.listdir(directory)
                if target_file in files_in_directory:
                    self.arrcon_exe_result_label.config(text=f"{target_file} detected", foreground="green")
                else:
                    self.arrcon_exe_result_label.config(text=f"{target_file} not found", foreground="red")
                    messagebox.showinfo("Invalid Directory", "ARRCON.exe was not found in the selected directory")
            else:
                self.arrcon_exe_result_label.config(text=f"{target_file} not found", foreground="red")
        elif target_file == "steamcmd.exe":
            if not directory == "No directory selected":
                files_in_directory = os.listdir(directory)
                if target_file in files_in_directory:
                    self.steamcmd_exe_result_label.config(text=f"{target_file} detected", foreground="green")
                else:
                    self.steamcmd_exe_result_label.config(text=f"{target_file} not found", foreground="red")
                    messagebox.showinfo("Invalid Directory", "steamcmd.exe was not found in the selected directory")
            else:
                self.steamcmd_exe_result_label.config(text=f"{target_file} not found", foreground="red")

        
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
                messagebox.showinfo("Invalid Directory", "You need to select a valid directory first")
        else:
            self.append_to_output("You need to select a valid directory first.")
            messagebox.showinfo("Invalid Directory", "You need to select a valid directory first")

    def get_server_info(self, directory):
        if not directory == "No directory selected":
            file_path = os.path.join(directory, 'Pal', 'Saved', 'Config', 'WindowsServer', 'PalWorldSettings.ini')
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding="utf-8") as file:
                    file_content = file.read()
                    max_players_match = re.search(r'ServerPlayerMaxNum=(\d+),', file_content)
                    server_name_match = re.search(r'ServerName="([^"]+)",', file_content)
                    server_description_match = re.search(r'ServerDescription="([^"]+)",', file_content)
                    server_password_match = re.search(r'ServerPassword="([^"]*)",', file_content)
                    server_port_match = re.search(r'PublicPort=(\d+),', file_content)
                    rcon_port_match = re.search(r'RCONPort=(\d+),', file_content)
                    rcon_enable_match = re.search(r'RCONEnabled=(\w+),', file_content)
                    rcon_password_match = re.search(r'AdminPassword="([^"]*)",', file_content)
                    if rcon_port_match:
                        port = int(rcon_port_match.group(1))
                        self.rcon_port.config(text=port)
                    if rcon_enable_match:
                        state = str(rcon_enable_match.group(1))
                        self.rcon_state.config(text=state)
                    if rcon_password_match:
                        rcon_pass = str(rcon_password_match.group(1))
                        if rcon_pass == "":
                            self.rcon_password.config(text="No Password Set")
                        else:
                            self.rcon_password.config(text="********")
                    if max_players_match:
                        max_players = int(max_players_match.group(1))
                        self.max_players.config(text=max_players)
                    if server_name_match:
                        server = str(server_name_match.group(1))
                        self.server_name.config(text=server)
                    if server_description_match:
                        description = str(server_description_match.group(1))
                        self.server_description.config(text=description)
                    if server_password_match:
                        serv_pass = str(server_password_match.group(1))
                        if serv_pass == "":
                            self.server_password.config(text="No Password Set")
                        else:
                            self.server_password.config(text=serv_pass)
                    if server_port_match:
                        serv_port = int(server_port_match.group(1))
                        self.server_port.config(text=serv_port)
            else:
                # reset_server_info()
                pass
        else:
            # reset_server_info()
            pass

form = Form()
