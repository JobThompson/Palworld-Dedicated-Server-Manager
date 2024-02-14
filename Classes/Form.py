from datetime import datetime

class Form:
    """Class to handle inputs in the interface form."""
    def __init__(self):
        self.restart_entry = None
        self.restart_schedule_entry = None
        self.monitor_interval_checkbox_var = None
        self.ampm_var = None
        self.monitor_entry = None
        self.backup_interval_entry = None
        
        self.output_text = None
        
    def append_to_output(self, message):
        """Function that sends message to output window"""
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        formatted_message = timestamp + message
        self.output_text.insert("end", formatted_message + "\n")
        self.output_text.yview("end")  # Auto-scroll to the bottom

form = Form()
