import os
import json

class Config:
    def __init__(self):
        self.config_directory = self.get_or_create_config_directory()
        self.config_file_path= os.path.join(self.config_directory, "config.json")
        # self.load_config()
        
    def get_or_create_config_directory(self):
        config_directory = os.path.join("./", "Config")
        if not os.path.exists(config_directory):
            os.makedirs(config_directory)
        return config_directory
    
    def save_config(self):
        try:
            settings = {
                "restart_entry": self.restart_entry.get(),
                "restart_schedule_entry": self.restart_schedule_entry.get(),
                "restart_time_entry": self.restart_time_entry.get(),
                "ampm_var": self.ampm_var.get(),
                "monitor_entry": self.monitor_entry.get(),
                "backup_interval_entry": self.backup_interval_entry.get(),
                "server_directory_selection": self.server_directory_selection.cget("text"),
                "arrcon_directory_selection": self.arrcon_directory_selection.cget("text"),
                "steamcmd_directory_selection": self.steamcmd_directory_selection.cget("text"),
                "backup_directory_selection": self.backup_directory_selection.cget("text"),
                "server_start_args_entry": self.server_start_args_entry.get(),
                "send_email_checkbox": self.send_email_checkbox.get(),
                "email_address_entry": self.email_address_entry.get(),
                "discordEntry": self.discordEntry.get(),
                "smtp_server_entry": self.smtp_server_entry.get(),
                "smtp_port_entry": self.smtp_port_entry.get()
            }
            with open(self.config_file_path, "w") as file:
                json.dump(settings, file)
        except Exception as e:
            print("Error saving settings: " + str(e))
            
    # def load_settings(self):
    #     try:
    #         with open(self.config_directory, "r") as file:
    #             config = json.load(file)
    #             restartEntry.insert(0, config.get("restartEntry", ""))
    #             restartScheduleEntry.insert(0, config.get("restartScheduleEntry", ""))
    #             ampm_var.set(config.get("ampm_var", "AM"))
    #             monitorEntry.insert(0, config.get("monitorEntry", ""))
    #             server_directory_selection.config(text=config.get("server_directory_selection", "No directory selected"))
    #             arrcon_directory_selection.config(text=config.get("arrcon_directory_selection", "No directory selected"))
    #             steamcmd_directory_selection.config(text=config.get("steamcmd_directory_selection", "No directory selected"))
    #             backup_directory_selection.config(text=config.get("backup_directory_selection", "No directory selected"))
    #             server_start_args_entry.insert(0, config.get("server_start_args_entry", '-useperfthreads -NoAsyncLoadingThread -UseMultithreadForDS -EpicApp=PalServer'))
    #             email_address_entry.insert(0, config.get("email_address_entry", ""))
    #             discordEntry.insert(0, config.get("discordEntry", ""))
    #             smtp_server_entry.insert(0, config.get("smtp_server_entry", "smtp.gmail.com"))
    #             smtp_port_entry.insert(0, config.get("smtp_port_entry", "587"))
    #     except FileNotFoundError:
    #         append_to_output("First time startup. Applying default configuration")
    #         server_directory_selection.config(text="No directory selected", foreground="red")
    #         arrcon_directory_selection.config(text="No directory selected", foreground="red")
    #         steamcmd_directory_selection.config(text="No directory selected", foreground="red")
    #         backup_directory_selection.config(text="No directory selected", foreground="red")
    #         server_start_args_entry.insert(0, '-useperfthreads -NoAsyncLoadingThread -UseMultithreadForDS -EpicApp=PalServer')
    #         smtp_server_entry.insert(0, "smtp.gmail.com")
    #         smtp_port_entry.insert(0, "587")


config_object = Config()