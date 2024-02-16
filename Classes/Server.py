from Classes.Form import form

class Server:
    """Server class to store server information and operate on server data"""
    def __init__(self, name, ip, port):
        self.name = name
        self.ip = ip
        self.port = port
        self.status = "offline"
        
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

