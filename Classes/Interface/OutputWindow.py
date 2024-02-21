from customtkinter import CTkTextbox
from datetime import datetime

class OutputWindow(CTkTextbox):
    """Output window class. This class handles the output window for the program."""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def append_to_output(self, message):
        """Function that sends message to output window"""
        self.configure(state="normal") # Allows editing
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        formatted_message = f'{timestamp} : {message}'
        self.insert("end", formatted_message + "\n")
        self.yview("end")
        self.configure(state="disabled") # Disabled editing
