from Classes.Form import form
import re
import subprocess
import os

class Server:
    """Server class to store server information and operate on server data"""
    def __init__(self, name):
        self.name = name
        # self.interface = interface
        self.current_function = ""
        
        self.rcon_pass = ''
        self.arrcon_exe_path = '../ARRCON/ARRCON.exe'
        self.rcon_port = ''
        self.palworld_directory = ''
        self.server_start_args = ''
        self.arrcon_command_save_server = ''
        self.arrcon_command_info_server = ''
        self.arrcon_command_shutdown_server = ''
        self.arrcon_command_server_message_30 = ''
        self.arrcon_command_server_message_10 = ''
        self.start_server_command = ''
        self.shutdown_server_command = ''
        self.force_shutdown_server_command = ''

    def get_rcon_info(self):
        """Pull the RCON password and port from the server's config file."""
        # Pull this from the local files? In order to use the RCON commands, a password and port has to be set in the server's config file.
        self.rcon_port = ''
        self.rcon_pass = ''
        
    def define_server_command_values(self):
        """Defines the values needed for server commands based on form data"""
        self.rcon_port = form.rcon_port.cget("text")
        self.palworld_directory = form.server_directory_selection.cget("text")
        self.server_start_args = form.server_start_args_entry.get()

    def get_arrcon_command(self, command):
        """Returns the command to be executed based on the command passed in."""
        match command:
            case "save":
                return f'{self.arrcon_exe_path} -H 127.0.0.1 -P {self.rcon_port} -p {self.rcon_pass} "save"'
            case "info":
                return f'{self.arrcon_exe_path} -H 127.0.0.1 -P {self.rcon_port} -p {self.rcon_pass} "info"'
            case "shutdown":
                return f'{self.arrcon_exe_path} -H 127.0.0.1 -P {self.rcon_port} -p {self.rcon_pass} "shutdown 60 The_server_will_be_restarting_in_60_seconds"'
            case "message_30":
                return f'{self.arrcon_exe_path} -H 127.0.0.1 -P {self.rcon_port} -p {self.rcon_pass} "broadcast The_server_will_be_restarting_in_30_seconds"'
            case "message_10":
                return  f'{self.arrcon_exe_path} -H 127.0.0.1 -P {self.rcon_port} -p {self.rcon_pass} "broadcast The_server_will_be_restarting_in_10_seconds"'
            case "start":
                return f'{self.palworld_directory}/PalServer.exe {self.server_start_args}'
            case "shutdown":
                return f'{self.arrcon_exe_path} -H 127.0.0.1 -P {self.rcon_port} -p {self.rcon_pass} "shutdown 5 The_server_will_be_shutting_down_in_5_seconds"'
            case "force_shutdown":
                return f'{self.arrcon_exe_path} -H 127.0.0.1 -P {self.rcon_port} -p {self.rcon_pass} "doexit"'
            case _:
                return "Invalid command"

    def save_server(self):
        """Saves the Palworld server"""
        form.append_to_output("Saving Palworld Server...")
        # self.interface.root.update()
        try:
            subprocess.Popen(self.get_arrcon_command("save"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            form.append_to_output("Palworld server was saved successfully...")
        except subprocess.CalledProcessError as e:
            form.append_to_output(f"Couldn't save the server due to error: {str(e)}")

    def shutdown_server(self, shutdown_type):
        """Shuts down the Palworld server"""
        if shutdown_type == "graceful":
            try:
                subprocess.Popen(self.get_arrcon_command("shutdown"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except subprocess.CalledProcessError as e:
                form.append_to_output(f"Couldn't shutdown the server due to error: {str(e)}")
        if shutdown_type == "force":
            try:
                subprocess.Popen(self.get_arrcon_command("force_shutdown"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except subprocess.CalledProcessError as e:
                form.append_to_output(f"Couldn't shutdown the server due to error: {str(e)}")

    def message_server_30(self, restartinterval):
        self.current_function = "message_server_30"
        subprocess.Popen(self.get_arrcon_command("message_30"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # form.after_id = root.after(20000, lambda: self.message_server_10(restartinterval))

    def scheduled_message_server_30(self):
        self.current_function = "message_server_30"
        subprocess.Popen(self.get_arrcon_command("message_30"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # form.after_id = form.root.after(20000, self.scheduled_message_server_10)

    def message_server_10(self, restartinterval):
        self.current_function = "message_server_10"
        try:
            subprocess.Popen(self.get_arrcon_command("message_10"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except Exception as e:
            form.append_to_output(f"Couldn't send message to the server due to error: " + str(e))
        # form.after_id = root.after(20000, lambda: self.restart_server(restartinterval))

    def scheduled_message_server_10(self):
        self.current_function = "message_server_10"
        try:
            subprocess.Popen(self.get_arrcon_command("message_10"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # self.after_id = root.after(20000, self.scheduled_restart_server)
        except Exception as e:
            form.append_to_output(f"Couldn't send message to the server due to error: " + str(e))
        
    def select_palworld_directory(self):
        """Open a file dialog to select the PalWorld directory."""
        directory_path = form.get_directory()
        if directory_path:
            form.server_directory_selection.config(text=f"{directory_path}", foreground="black")
            self.search_file(directory_path, "PalServer.exe")
            self.get_server_info(directory_path)
        else:
            form.server_directory_selection.config(text="No directory selected", foreground="red")
            form.palworld_exe_result_label.config(text="PalServer.exe not found", foreground="red")
            form.append_to_output("The directory you selected does not contain the PalServer.exe and other file information required to run this application. Please verify the directory")
            form.open_modal("Invalid Directory", "PalServer.exe was not found in the selected directory")
            
    def select_arrcon_directory(self):
        directory_path = form.get_directory()
        if directory_path:
            form.arrcon_directory_selection.config(text=f"{directory_path}", foreground="black")
            self.search_file(directory_path, "ARRCON.exe")
        else:
            form.arrcon_directory_selection.config(text="No directory selected", foreground="red")
            form.arrcon_exe_result_label.config(text="ARRCON.exe not found", foreground="red")
            form.append_to_output("The directory you selected does not contain the ARRCON.exe required to run this application. Please verify the directory")
            form.open_modal("Invalid Directory", "ARRCON.exe was not found in the selected directory")

    def select_steamcmd_directory(self):
        directory_path = form.get_directory()
        if directory_path:
            form.steamcmd_directory_selection.config(text=f"{directory_path}", foreground="black")
            self.search_file(directory_path, "steamcmd.exe")
        else:
            form.steamcmd_directory_selection.config(text="No directory selected", foreground="red")
            form.steamcmd_exe_result_label.config(text="steamcmd.exe not found", foreground="red")
            form.append_to_output("The directory you selected does not contain the steamcmd.exe. Please verify the directory")
            form.open_modal("Invalid Directory", "steamcmd.exe was not found in the selected directory")

    def select_backup_directory(self):
        directory_path = form.get_directory()
        if directory_path:
            form.backup_directory_selection.config(text=f"{directory_path}", foreground="black")
        else:
            form.backup_directory_selection.config(text="No directory selected", foreground="red")


    def search_file(self, directory, target_file):
        """Search for a file in the selected directory."""
        if target_file == "PalServer.exe":
            if not directory == "No directory selected":
                files_in_directory = os.listdir(directory)
                if target_file in files_in_directory:
                    form.palworld_exe_result_label.config(text=f"{target_file} detected", foreground="green")
                else:
                    form.palworld_exe_result_label.config(text=f"{target_file} not found", foreground="red")
                    form.open_modal("Invalid Directory", "PalServer.exe was not found in the selected directory")
            else:
                form.palworld_exe_result_label.config(text=f"{target_file} not found", foreground="red")
        elif target_file == "ARRCON.exe":
            if not directory == "No directory selected":
                files_in_directory = os.listdir(directory)
                if target_file in files_in_directory:
                    form.arrcon_exe_result_label.config(text=f"{target_file} detected", foreground="green")
                else:
                    form.arrcon_exe_result_label.config(text=f"{target_file} not found", foreground="red")
                    form.open_modal("Invalid Directory", "ARRCON.exe was not found in the selected directory")
            else:
                form.arrcon_exe_result_label.config(text=f"{target_file} not found", foreground="red")
        elif target_file == "steamcmd.exe":
            if not directory == "No directory selected":
                files_in_directory = os.listdir(directory)
                if target_file in files_in_directory:
                    form.steamcmd_exe_result_label.config(text=f"{target_file} detected", foreground="green")
                else:
                    form.steamcmd_exe_result_label.config(text=f"{target_file} not found", foreground="red")
                    form.open_modal("Invalid Directory", "steamcmd.exe was not found in the selected directory")
            else:
                form.steamcmd_exe_result_label.config(text=f"{target_file} not found", foreground="red")


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
                        form.rcon_state.config(text=state)
                    if rcon_password_match:
                        rcon_pass = str(rcon_password_match.group(1))
                        if rcon_pass == "":
                            form.rcon_password.config(text="No Password Set")
                        else:
                            form.rcon_password.config(text="********")
                    if max_players_match:
                        max_players = int(max_players_match.group(1))
                        form.max_players.config(text=max_players)
                    if server_name_match:
                        server = str(server_name_match.group(1))
                        form.server_name.config(text=server)
                    if server_description_match:
                        description = str(server_description_match.group(1))
                        form.server_description.config(text=description)
                    if server_password_match:
                        serv_pass = str(server_password_match.group(1))
                        if serv_pass == "":
                            form.server_password.config(text="No Password Set")
                        else:
                            form.server_password.config(text=serv_pass)
                    if server_port_match:
                        serv_port = int(server_port_match.group(1))
                        form.server_port.config(text=serv_port)
            else:
                self.reset_server_info()
        else:
            self.reset_server_info()


    def reset_server_info(self):
        """Reset the server info to default values."""
        form.rcon_port.config(text="-")
        form.rcon_state.config(text="-")
        form.max_players.config(text="-")
        form.server_name.config(text="-")
        form.server_description.config(text="-")
        form.server_password.config(text="-")
        form.server_port.config(text="-")


