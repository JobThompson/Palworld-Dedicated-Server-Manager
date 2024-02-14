import os
import json
from Classes.Form import form

class Config:
    def __init__(self):
        self.config_directory = self.get_or_create_config_directory()
        self.config_file_path= os.path.join(self.config_directory, "config.json")

        self.arrcon_exe_path = '../ARRCON/ARRCON.exe'
        self.palworld_directory = None

        self.rcon_getport = None # rcon_port.cget("text")
        self.rcon_pass = None # re.search(r'AdminPassword="([^"]*)",', file_content).group(1)
        self.server_start_args = None # server_start_args_entry.get()
        self.arrcon_command_save_server = f'{self.arrcon_exe_path} -H 127.0.0.1 -P {self.rcon_getport} -p {self.rcon_pass} "save"'
        self.arrcon_command_info_server = f'{self.arrcon_exe_path} -H 127.0.0.1 -P {self.rcon_getport} -p {self.rcon_pass} "info"'
        self.arrcon_command_shutdown_server = f'{self.arrcon_exe_path} -H 127.0.0.1 -P {self.rcon_getport} -p {self.rcon_pass} "shutdown 60 The_server_will_be_restarting_in_60_seconds"'
        self.arrcon_command_server_message_30 = f'{self.arrcon_exe_path} -H 127.0.0.1 -P {self.rcon_getport} -p {self.rcon_pass} "broadcast The_server_will_be_restarting_in_30_seconds"'
        self.arrcon_command_server_message_10 = f'{self.arrcon_exe_path} -H 127.0.0.1 -P {self.rcon_getport} -p {self.rcon_pass} "broadcast The_server_will_be_restarting_in_10_seconds"'
        self.start_server_command = f'{self.palworld_directory}/PalServer.exe {self.server_start_args}'
        self.shutdown_server_command = f'{self.arrcon_exe_path} -H 127.0.0.1 -P {self.rcon_getport} -p {self.rcon_pass} "shutdown 5 The_server_will_be_shutting_down_in_5_seconds"'
        self.force_shutdown_server_command = f'{self.arrcon_exe_path} -H 127.0.0.1 -P {self.rcon_getport} -p {self.rcon_pass} "doexit"'

        # self.load_config()

    def get_or_create_config_directory(self):
        config_directory = os.path.join("./", "Config")
        if not os.path.exists(config_directory):
            os.makedirs(config_directory)
        return config_directory

    def save_config(self):
        try:
            settings = {
                "restart_entry": form.restart_entry.get(),
                "restart_schedule_entry": form.restart_schedule_entry.get(),
                "monitor_interval_checkbox_var": form.monitor_interval_checkbox_var.get(),
                "ampm_var": form.ampm_var.get(),
                "monitor_entry": form.monitor_entry.get(),
                "backup_interval_entry": form.backup_interval_entry.get(),
                # "server_directory_selection": form.server_directory_selection.cget("text"),
                # "arrcon_directory_selection": form.arrcon_directory_selection.cget("text"),
                # "steamcmd_directory_selection": form.steamcmd_directory_selection.cget("text"),
                # "backup_directory_selection": form.backup_directory_selection.cget("text"),
                # "server_start_args_entry": form.server_start_args_entry.get(),
                # "send_email_checkbox": form.send_email_checkbox.get(),
                # "email_address_entry": form.email_address_entry.get(),
                # "discord_entry": form.discord_entry.get(),
                # "smtp_server_entry": form.smtp_server_entry.get(),
                # "smtp_port_entry": form.smtp_port_entry.get()
            }
            with open(self.config_file_path, "w", encoding="utf-8") as file:
                json.dump(settings, file)
        except FileNotFoundError as e:
            print("Error saving settings: " + str(e))
        except IOError as e:
            print("Error saving settings: " + str(e))

    def load_config(self):
        try:
            with open(self.config_file_path, "r", encoding="utf-8") as file:
                config = json.load(file)
                # form.restart_entry.insert(0, config.get("restart_entry", ""))
                # form.restart_schedule_entry.insert(0, config.get("restart_schedule_entry", ""))
                # form.monitor_interval_checkbox_var.insert(False, "monitor_interval_checkbox_var")
                # form.ampm_var.set(config.get("ampm_var", "AM"))
                # form.monitor_entry.insert(0, config.get("monitor_entry", ""))
                # form.backup_interval_entry.insert(0, config.get("backup_interval_entry", ""))
                # server_directory_selection.config(text=config.get("server_directory_selection", "No directory selected"))
                # arrcon_directory_selection.config(text=config.get("arrcon_directory_selection", "No directory selected"))
                # steamcmd_directory_selection.config(text=config.get("steamcmd_directory_selection", "No directory selected"))
                # backup_directory_selection.config(text=config.get("backup_directory_selection", "No directory selected"))
                # server_start_args_entry.insert(0, config.get("server_start_args_entry", '-useperfthreads -NoAsyncLoadingThread -UseMultithreadForDS -EpicApp=PalServer'))
                # email_address_entry.insert(0, config.get("email_address_entry", ""))
                # discordEntry.insert(0, config.get("discordEntry", ""))
                # smtp_server_entry.insert(0, config.get("smtp_server_entry", "smtp.gmail.com"))
                # smtp_port_entry.insert(0, config.get("smtp_port_entry", "587"))
        except FileNotFoundError:
            pass
            # append_to_output("First time startup. Applying default configuration")
            # server_directory_selection.config(text="No directory selected", foreground="red")
            # arrcon_directory_selection.config(text="No directory selected", foreground="red")
            # steamcmd_directory_selection.config(text="No directory selected", foreground="red")
            # backup_directory_selection.config(text="No directory selected", foreground="red")
            # server_start_args_entry.insert(0, '-useperfthreads -NoAsyncLoadingThread -UseMultithreadForDS -EpicApp=PalServer')
            # smtp_server_entry.insert(0, "smtp.gmail.com")
            # smtp_port_entry.insert(0, "587")


config_object = Config()
