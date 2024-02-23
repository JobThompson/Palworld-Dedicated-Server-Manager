import subprocess
import psutil

class ServerHandler:
    def __init__(self) -> None:
        self.after_id = None
        self.task_name = "PalServer-Win64-Test-Cmd.exe"
    
    def get_server_attributes(self, form):
        pass
    
    def start_server(self, form):
        command = f'{form.palworld_directory_label.cget("text")}/PalServer.exe {form.server_startup_args_entry.get()}'
        
    def save_server(self, form):
        command = f'{form.arrcon_directory_label.cget("text")}/ARRCON.exe -H 127.0.0.1 -P {form.server_rcon_port.cget("text")} -p {form.server_rcon_password.cget("text")} "save"'
    
    def get_info(self, form):
        command = f'{form.arrcon_directory_label.cget("text")}/ARRCON.exe -H 127.0.0.1 -P {form.server_rcon_port.cget("text")} -p {form.server_rcon_password.cget("text")} "info"'
    
    def graceful_stop_server(self, form, delay = '5', server_message = ""):
        command = f'{form.arrcon_directory_label.cget("text")}/ARRCON.exe -H 127.0.0.1 -P {form.server_rcon_port.cget("text")} -p {form.server_rcon_password.cget("text")} "shutdown {delay} {server_message}"'
        
    def force_stop_server(self, form):
        command = f'{form.arrcon_directory_label.cget("text")}/ARRCON.exe -H 127.0.0.1 -P {form.server_rcon_port.cget("text")} -p {form.server_rcon_password.cget("text")} "doexit"'
        [proc for proc in psutil.process_iter(['pid', 'name']) if proc.name() == self.task_name][0].kill()
        
    def restart_server(self, form):
        form.write_output("Restarting Server")
        self.graceful_stop_server(form, None, "The_server_will_be_shutting_down_in_5_seconds")
        self.start_server(form)
        
    def send_server_message(self, form, message):
        command = f'{form.arrcon_directory_label.cget("text")}/ARRCON.exe -H 127.0.0.1 -P {form.server_rcon_port.cget("text")} -p {form.server_rcon_password.cget("text")} "boadcast {message}"'
    
    def monitor_server(self, form):
        pass
    
    def backup_server(self, form):
        pass
    
    def update_server(self, form):
        if [proc for proc in psutil.process_iter(['pid', 'name']) if proc.name() == self.task_name]:
            form.write_output("The server is running, shutting down the server to update.")
            self.graceful_stop_server(form, None, "The_server_will_be_shutting_down_in_5_seconds")
            
        command = f"call {form.steamcmd_directory_label.cget('text')}/steamcmd.exe +force_install_dir {form.palworld_directory_label.cget('text')} +login anonymous +app_update 2394010 +quit"
        process = self.execute_command(command)
        return_code = process.wait()
        if return_code == 0:
            form.write_output("The server has updated successfully")
        else:
            form.write_output("The server has failed to update")
    
    def open_server_directory(self, form):
        pass
    
    def execute_command(self, command):
        return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)