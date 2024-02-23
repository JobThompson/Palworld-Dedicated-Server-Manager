from customtkinter import CTkFrame, CTkLabel, CTkEntry

class ServerFunctionConfiguration(CTkFrame):
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.label_font = ("Arial", 12, "bold")
    
    def create_server_function_configuration(self, form):
        """Create the server function configuration widgets."""
        # Column 0
        server_restart_interval_label = CTkLabel(self, text="Server Restart Interval", fg_color="transparent")
        server_restart_interval_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        daily_restart_time_label = CTkLabel(self, text="Daily Restart Time (24H)", fg_color="transparent")
        daily_restart_time_label.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        backup_interval_label = CTkLabel(self, text="Backup Interval", fg_color="transparent")
        backup_interval_label.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")

        monitor_interval_label = CTkLabel(self, text="Monitor Interval", fg_color="transparent")
        monitor_interval_label.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")

        # Column 1
        form.server_restart_interval = CTkEntry(self, width=120)
        form.server_restart_interval.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="w")

        form.daily_restart_time = CTkEntry(self, width=120)
        form.daily_restart_time.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="w")

        form.backup_interval = CTkEntry(self, width=120)
        form.backup_interval.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="w")

        form.monitor_interval = CTkEntry(self, width=120)
        form.monitor_interval.grid(row=3, column=1, padx=10, pady=(10, 0), sticky="w")
        