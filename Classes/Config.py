import os
import json

class Config():
    """Config import and export class for the application"""
    def __init__(self):
        self.config_directory = self.get_or_create_config_directory()
        self.config_file_path = os.path.join(self.config_directory, "config.json")
    
    def get_or_create_config_directory(self):
        """Returns the path to the config directory, creating it if it doesn't exist."""
        config_directory = os.path.join("./", "Config")
        if not os.path.exists(config_directory):
            os.makedirs(config_directory)
        return config_directory
    
    def import_config(self, form):
        """Function to import the configuration file"""
        print("Importing Config")
        try:
            with open(self.config_file_path, "r", encoding="utf-8") as file:
                form_data = json.load(file)
                form.palworld_directory_label.configure(text=form_data["palworld_directory"])
                form.arrcon_directory_label.configure(text=form_data["arrcon_directory"])
                form.steamcmd_directory_label.configure(text=form_data["steamcmd_directory"])
                form.backup_directory_label.configure(text=form_data["backup_directory"])
                form.server_startup_args_entry.insert(0, form_data["server_startup_args"])
                form.server_restart_interval.insert(0, form_data["server_restart_interval"])
                form.daily_restart_time.insert(0, form_data["daily_restart_time"])
                form.backup_interval.insert(0, form_data["backup_interval"])
                form.monitor_interval.insert(0, form_data["monitor_interval"])
                form.send_notification_email.set(form_data["send_notification_email"])
                form.send_notification_discord.set(form_data["send_notification_discord"])
                form.send_backup_notification.set(form_data["send_backup_notification"])
                form.notification_email.insert(0, form_data["notification_email"])
                form.notification_email_password.insert(0, form_data["notification_email_password"])
                form.smtp_server.insert(0, form_data["smtp_server"])
                form.smtp_port.insert(0, form_data["smtp_port"])
                form.notification_discord_webhook.insert(0, form_data["notification_discord_webhook"])
        except FileNotFoundError:
            print("Config file not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON")
        except Exception as e:
            print("Error importing config:", e)


    def export_config(self, form):
        """Function to export the configuration file"""
        print("Exporting Config")
        try:
            with open(self.config_file_path, "w", encoding="utf-8") as file:
                json.dump({
                    "palworld_directory": form.palworld_directory_label.cget("text"),
                    "arrcon_directory": form.arrcon_directory_label.cget("text"),
                    "steamcmd_directory": form.steamcmd_directory_label.cget("text"),
                    "backup_directory": form.backup_directory_label.cget("text"),
                    "server_startup_args": form.server_startup_args_entry.get(),
                    "server_restart_interval": form.server_restart_interval.get(),
                    "daily_restart_time": form.daily_restart_time.get(),
                    "backup_interval": form.backup_interval.get(),
                    "monitor_interval": form.monitor_interval.get(),
                    "send_notification_email": form.send_notification_email.get(),
                    "send_notification_discord": form.send_notification_discord.get(),
                    "send_backup_notification": form.send_backup_notification.get(),
                    "notification_email": form.notification_email.get(),
                    "notification_email_password": form.notification_email_password.get(),
                    "smtp_server": form.smtp_server.get(),
                    "smtp_port": form.smtp_port.get(),
                    "notification_discord_webhook": form.notification_discord_webhook.get()
                    }, file)
        except FileNotFoundError:
            print("Config file not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON")
        except Exception as e:
            print("Error exporting config:", e)