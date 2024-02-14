from tkinter import Tk, ttk, N, W, E, S, StringVar, LabelFrame, BooleanVar

class Interface:
    def __init__(self) -> None:
        self.root = Tk()
        self.mainframe = None
        self.tabControl = None
        
        self.configure_main_window_size()
        self.create_tabs()
        self.config_main_tab()
        self.config_server_config_tab()
        self.start_mainloop()
    
    def configure_main_window_size(self):
        self.root.title("PalWorld Server Manager")
        self.root.geometry("800x600")
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        
    def create_tabs(self):
        self.tabControl = ttk.Notebook(self.root)
        self.main_tab = ttk.Frame(self.tabControl) 
        self.server_config_tab = ttk.Frame(self.tabControl)
        self.alerts_config_tab = ttk.Frame(self.tabControl)
        self.about_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.main_tab, text ='Main') 
        self.tabControl.add(self.server_config_tab, text ='Server Config')
        self.tabControl.add(self.alerts_config_tab, text ='Alerts Config') 
        self.tabControl.add(self.about_tab, text ='About') 
        self.tabControl.pack(expand = 1, fill ="both")
        self.main_tab.columnconfigure(0, weight=1)
        self.main_tab.columnconfigure(1, weight=1)
        self.server_config_tab.columnconfigure(0, weight=1)
        self.alerts_config_tab.columnconfigure(0, weight=1)
        self.alerts_config_tab.columnconfigure(1, weight=1)
        self.about_tab.columnconfigure(0, weight=1)
                
    def config_main_tab(self):
        self.main_interval_frame = LabelFrame(self.main_tab, text="Interval Configuration")
        self.main_interval_frame.grid(column=0, row=0, padx=10, pady=10, sticky=(N, W, E, S))
        restart_interval_checkbox_var = BooleanVar()
        restart_interval_checkbox = ttk.Checkbutton(self.main_interval_frame, variable=restart_interval_checkbox_var, command="enable_server_restart")
        restart_interval_checkbox.grid(column=0, row=0)
        restartLabel = ttk.Label(self.main_interval_frame, text="Server Restart Interval (hours):")
        restartLabel.grid(column=1, row=0, sticky=(W))
        restartEntry = ttk.Entry(self.main_interval_frame, width=3)
        restartEntry.grid(column=2, row=0, sticky=(W))

        restartScheduleCheckbox_var = BooleanVar()
        restartScheduleCheckbox = ttk.Checkbutton(self.main_interval_frame, variable=restartScheduleCheckbox_var, command="enable_scheduled_restart")
        restartScheduleCheckbox.grid(column=0, row=1)
        restartScheduleLabel = ttk.Label(self.main_interval_frame, text="Daily Server Restart Time (12-hour Format):")
        restartScheduleLabel.grid(column=1, row=1, sticky=(W))
        restartTimeEntry_var = StringVar()
        restartScheduleEntry = ttk.Entry(self.main_interval_frame, textvariable=restartTimeEntry_var, width=6)
        restartScheduleEntry.grid(column=2, row=1, sticky=(W))
        ampm_var = StringVar(value="AM")
        ampm_combobox = ttk.Combobox(self.main_interval_frame, textvariable=ampm_var, values=["AM", "PM"], width=4)
        ampm_combobox.grid(column=3, row=1)

        monitor_interval_checkbox_var = BooleanVar()
        monitor_interval_checkbox = ttk.Checkbutton(self.main_interval_frame, variable=monitor_interval_checkbox_var, command="enable_monitor_server")
        monitor_interval_checkbox.grid(column=0, row=2)
        monitorLabel = ttk.Label(self.main_interval_frame, text="Monitor Interval (minutes):")
        monitorLabel.grid(column=1, row=2, sticky=(W))
        monitorEntry = ttk.Entry(self.main_interval_frame, width=3)
        monitorEntry.grid(column=2, row=2, sticky=(W))

        backupIntervalCheckbox_var = BooleanVar()
        backupIntervalCheckbox = ttk.Checkbutton(self.main_interval_frame, variable=backupIntervalCheckbox_var, command="enable_backup_interval")
        backupIntervalCheckbox.grid(column=0, row=3)
        backupIntervalLabel = ttk.Label(self.main_interval_frame, text="Backup Server Interval (hours):")
        backupIntervalLabel.grid(column=1, row=3, sticky=(W))
        backupIntervalEntry = ttk.Entry(self.main_interval_frame, width=3)
        backupIntervalEntry.grid(column=2, row=3, sticky=(W))
        
    def config_server_config_tab(self):
        self.optional_config_frame = LabelFrame(self.main_tab, text="Optional Configurations")
        self.optional_config_frame.grid(column=0, row=1, padx=10, pady=10, sticky=(N, W, E, S))

        send_email_checkbox_var = BooleanVar()
        send_email_checkbox = ttk.Checkbutton(self.optional_config_frame, variable=send_email_checkbox_var, command="enable_send_email")
        send_email_checkbox.grid(column=0, row=0)
        send_email_label = ttk.Label(self.optional_config_frame, text="Send Notification Email on crash")
        send_email_label.grid(column=1, row=0, sticky=(W))

        discordWebhookCheckbox_var = BooleanVar()
        discordWebhookCheckbox = ttk.Checkbutton(self.optional_config_frame, variable=discordWebhookCheckbox_var, command="enable_send_discord_message")
        discordWebhookCheckbox.grid(column=0, row=1)
        discordWebhookLabel = ttk.Label(self.optional_config_frame, text="Send Discord channel message on crash")
        discordWebhookLabel.grid(column=1, row=1, sticky=(W))

        update_server_startup_checkbox_var = BooleanVar()
        update_server_startup_checkbox = ttk.Checkbutton(self.optional_config_frame, variable=update_server_startup_checkbox_var, command="enable_server_updates_on_startup")
        update_server_startup_checkbox.grid(column=0, row=2)
        update_server_startup_label = ttk.Label(self.optional_config_frame, text="Check for updates on startup")
        update_server_startup_label.grid(column=1, row=2, sticky=(W))

        backup_server_checkbox_var = BooleanVar()
        backup_server_checkbox = ttk.Checkbutton(self.optional_config_frame, variable=backup_server_checkbox_var, command="enable_server_backups")
        backup_server_checkbox.grid(column=0, row=3)
        backup_server_label = ttk.Label(self.optional_config_frame, text="Backup server during restarts")
        backup_server_label.grid(column=1, row=3, sticky=(W))

        deleteOldBackupsCheckbox_var = BooleanVar()
        deleteOldBackupsCheckbox = ttk.Checkbutton(self.optional_config_frame, variable=deleteOldBackupsCheckbox_var, command="enable_delete_backups")
        deleteOldBackupsCheckbox.grid(column=0, row=4)
        deleteOldBackupsLabel = ttk.Label(self.optional_config_frame, text="Delete Backups Older Than (Days):")
        deleteOldBackupsLabel.grid(column=1, row=4, sticky=(W))
        deleteOldBackupsEntry = ttk.Entry(self.optional_config_frame, width=3)
        deleteOldBackupsEntry.grid(column=2, row=4, sticky=(W))

                
    def start_mainloop(self):
        self.root.mainloop()