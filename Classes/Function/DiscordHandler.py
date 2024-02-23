import requests
class DiscordHandler:
    """Handles all the discord related stuff."""
    def __init__(self) -> None:
        pass

    def send_discord_notification(self, form, message):
        """Post a message to the discord channel"""
        try:
            data = {
                "content": message
            }
            response = requests.post(form.notification_discord_webhook.get(), json=data, timeout=5)  # Added timeout argument
            response.raise_for_status()  # Check for HTTP errors

        except requests.exceptions.RequestException as e:
            form.append_to_output("Error posting discord message: " + str(e))

    def send_discord_crash_message(self, form):
        """Post a crash notification to the discord channel"""
        self.send_discord_notification(form, "The PalWorld server has crashed. It has been restarted.")

    def send_discord_backup_message(self, form):
        """Post a backup notification to the discord channel"""
        self.send_discord_notification(form, "The server was backed up successfully.")
    
