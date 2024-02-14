import requests

class DiscordHandler:
    """Handles all the discord related stuff."""
    def __init__(self, webhook_url = None) -> None:
        self.webhook_url = webhook_url

    def post_discord_message(self, message = "The PalWorld server has crashed. It has been restarted."):
        """Post a message to the discord channel"""
        if self.webhook_url is None:
            print("No discord webhook URL set. Please set the webhook URL in the settings.")
            return

        try:
            data = {
                "content": message
            }
            response = requests.post(self.webhook_url, json=data, timeout=5)  # Added timeout argument
            response.raise_for_status()  # Check for HTTP errors

        except requests.exceptions.RequestException as e:
            print("Error posting discord message: " + str(e))


discord_handler = DiscordHandler()