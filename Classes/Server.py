import re, psutil, subprocess, os, datetime, zipfile
from Classes.Form import form

TASK_NAME = "PalServer-Win64-Test-Cmd.exe"

class Server:
    """Server class to store server information and operate on server data"""
    def __init__(self):
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
    
    def check_palworld_process(self):
        task_name = "PalServer-Win64-Test-Cmd.exe"
        running_processes = [proc.name() for proc in psutil.process_iter()] # Get the list of running processes
        form.append_to_output("Server is now running") if task_name in running_processes else form.append_to_output("Server is not running") # Notify if the server is running or not
            
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

    def message_server_30(self, root, restartinterval):
        self.current_function = "message_server_30"
        subprocess.Popen(self.get_arrcon_command("message_30"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        form.after_id = root.after(20000, lambda: self.message_server_10(root, restartinterval))

    def scheduled_message_server_30(self, root):
        self.current_function = "message_server_30"
        subprocess.Popen(self.get_arrcon_command("message_30"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        form.after_id = root.after(20000, self.scheduled_message_server_10(root))

    def message_server_10(self, root, restartinterval):
        self.current_function = "message_server_10"
        try:
            subprocess.Popen(self.get_arrcon_command("message_10"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except Exception as e:
            form.append_to_output(f"Couldn't send message to the server due to error: " + str(e))
        form.after_id = root.after(20000, lambda: self.restart_server(restartinterval))

    def scheduled_message_server_10(self, root):
        self.current_function = "message_server_10"
        try:
            subprocess.Popen(self.get_arrcon_command("message_10"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            form.after_id = root.after(20000, self.scheduled_restart_server)
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
        
    def scheduled_restart_server(self, root):  # TODO: This can be used for both scheduled restarts and regular restarts.
        self.current_function = "restart_server"
        form.append_to_output("Palworld Server is shutdown. Checking for residual processes... Sometimes the server process gets stuck")
        root.update()
        
        # if form.enable_backups == True:
        #         self.backup_server()
        
        try:
            task_info = [proc for proc in psutil.process_iter(['pid', 'name']) if proc.name() == TASK_NAME] # Get the list of running processes that match the process name
            psutil.Process(task_info.info['pid']).terminate()
            form.append_to_output("Server process was terminated successfully...")
        except psutil.NoSuchProcess as e:
            form.append_to_output(f"Couldn't terminate the server process due to error: {str(e)}")
        except psutil.AccessDenied as e:
            form.append_to_output(f"Couldn't terminate the server process due to error: {str(e)}")
        except Exception as e:
            form.append_to_output(f"Couldn't terminate the server process due to error: {str(e)}")


    def backup_server(self):
        if not form.palworld_exe_result_label.cget("text") == "PalServer.exe not found":
            if not form.backup_directory_selection.cget("text") == "No directory selected":
                palworld_directory = form.server_directory_selection.cget("text")
                backup_dir = form.backup_directory_selection.cget("text")
                source_dir = f"{palworld_directory}/Pal/Saved/SaveGames/0"

                # Create the backup directory if it doesn't exist
                os.makedirs(backup_dir, exist_ok=True)

                # Get the current date and time
                current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

                # Compose the backup file path
                backup_file_path = os.path.join(backup_dir, f"palworld_backup_{current_datetime}.zip")

                files_to_backup = []
                for root, dirs, files in os.walk(source_dir):
                    files_to_backup.extend(os.path.join(root, file) for file in files)

                if files_to_backup:
                    with zipfile.ZipFile(backup_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_archive:
                        for root, dirs, files in os.walk(source_dir):
                            for file in files:
                                file_path = os.path.join(root, file)
                                arcname = os.path.relpath(file_path, source_dir)
                                zip_archive.write(file_path, arcname=arcname)

                # Print a message indicating the completion of the backup
                form.append_to_output(f"Backup of {source_dir} completed at {backup_file_path}")
                if form.delete_old_backups_checkbox_var.get():
                    # self.delete_old_backups()
                    pass
                else:
                    form.append_to_output("You must select a Backup Directory to use this function. Check your Server Config tab")
                    form.open_modal("Invalid Directory", "You must select a valid Backup directory to use this function")
            else:
                form.append_to_output("You must select a valid Palworld Server Directory to use this function. Check your Server Config tab")
                form.open_modal("Invalid Directory", "You must select a valid Palworld Server directory to use this function")
                
    def delete_old_backups(self):
        current_time = datetime.datetime.now()
        days_entry = int(form.delete_old_backups_entry.get())
        form.append_to_output(str(days_entry))

        days_ago = current_time - datetime.timedelta(days=days_entry)

        backup_dir = form.backup_directory_selection.cget("text")

        for filename in os.listdir(backup_dir):
            if filename.startswith("palworld_backup_"):
                filepath = os.path.join(backup_dir, filename)
            
                modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
            
                if modification_time < days_ago:
                    os.remove(filepath)
                    form.append_to_output(f"Old backup deleted: {filepath}")


server = Server()