from tkinter import Tk, ttk, N, W, E, S, StringVar, LabelFrame, BooleanVar, Frame, Text
from datetime import datetime
from Classes.Config import config_object

class Interface:
    """Class that handles the TKinter interface for the server manager"""
    def __init__(self) -> None:
        self.root = Tk()
        self.mainframe = None
        self.tab_control = None
        
        self.entry_width = 10
        
        self.set_favicon('palworld_logo.ico')
        self.configure_main_window_size()
        self.create_tabs()
        self.config_main_tab()
        self.config_optional_config_in_main_tab()
        self.config_server_functions_in_main_tab()
        self.create_output_window()
        self.set_exit_conditions()
        config_object.load_config()
        self.start_mainloop()
        
    def set_favicon(self, icon_path):
        try:
            self.root.iconbitmap(icon_path)
        except Exception as e:
            self.append_to_output("Icon wasn't able to load due to error: " + str(e))

    
    def configure_main_window_size(self):
        self.root.title("PalWorld Server Manager")
        self.root.geometry("800x600")
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        
        
    def create_tabs(self):
        self.tab_control = ttk.Notebook(self.root)
        self.main_tab = ttk.Frame(self.tab_control) 
        self.server_config_tab = ttk.Frame(self.tab_control)
        self.alerts_config_tab = ttk.Frame(self.tab_control)
        self.about_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.main_tab, text ='Main') 
        self.tab_control.add(self.server_config_tab, text ='Server Config')
        self.tab_control.add(self.alerts_config_tab, text ='Alerts Config') 
        self.tab_control.add(self.about_tab, text ='About') 
        self.tab_control.pack(expand = 1, fill ="both")
        self.main_tab.columnconfigure(0, weight=1)
        self.main_tab.columnconfigure(1, weight=1)
        self.server_config_tab.columnconfigure(0, weight=1)
        self.alerts_config_tab.columnconfigure(0, weight=1)
        self.alerts_config_tab.columnconfigure(1, weight=1)
        self.about_tab.columnconfigure(0, weight=1)


    def config_main_tab(self):
        main_interval_frame = LabelFrame(self.main_tab, text="Interval Configuration")
        main_interval_frame.grid(column=0, row=0, padx=10, pady=10, sticky=(N, W, E, S))
        restart_interval_checkbox_var = BooleanVar()
        restart_interval_checkbox = ttk.Checkbutton(main_interval_frame, variable=restart_interval_checkbox_var, command="enable_server_restart")
        restart_interval_checkbox.grid(column=0, row=0)
        restart_label = ttk.Label(main_interval_frame, text="Server Restart Interval (hours):")
        restart_label.grid(column=1, row=0, sticky=(W))
        config_object.restart_entry = ttk.Entry(main_interval_frame, width=self.entry_width)
        config_object.restart_entry.grid(column=2, row=0, sticky=(W))

        restart_schedule_checkbox_var = BooleanVar()
        restart_schedule_checkbox = ttk.Checkbutton(
            main_interval_frame,
            variable=restart_schedule_checkbox_var,
            command="enable_scheduled_restart"
        )
        restart_schedule_checkbox.grid(column=0, row=1)
        restart_schedule_label = ttk.Label(main_interval_frame, text="Daily Server Restart Time (12-hour Format):")
        restart_schedule_label.grid(column=1, row=1, sticky=(W))
        config_object.restart_schedule_entry = StringVar()
        restart_schedule_entry = ttk.Entry(main_interval_frame, textvariable=config_object.restart_schedule_entry, width=self.entry_width)
        restart_schedule_entry.grid(column=2, row=1, sticky=(W))
        config_object.ampm_var = StringVar(value="AM")
        ampm_combobox = ttk.Combobox(main_interval_frame, textvariable=config_object.ampm_var, values=["AM", "PM"], width=4)
        ampm_combobox.grid(column=3, row=1)

        config_object.monitor_interval_checkbox_var = BooleanVar()
        monitor_interval_checkbox = ttk.Checkbutton(main_interval_frame, variable=config_object.monitor_interval_checkbox_var, command="enable_monitor_server")
        monitor_interval_checkbox.grid(column=0, row=2)
        monitor_label = ttk.Label(main_interval_frame, text="Monitor Interval (minutes):")
        monitor_label.grid(column=1, row=2, sticky=(W))
        config_object.monitor_entry = ttk.Entry(main_interval_frame, width=self.entry_width)
        config_object.monitor_entry.grid(column=2, row=2, sticky=(W))

        config_object.backup_interval_checkbox_var = BooleanVar()
        backup_interval_checkbox = ttk.Checkbutton(main_interval_frame, variable=config_object.backup_interval_checkbox_var, command="enable_backup_interval")
        backup_interval_checkbox.grid(column=0, row=3)
        backup_interval_label = ttk.Label(main_interval_frame, text="Backup Server Interval (hours):")
        backup_interval_label.grid(column=1, row=3, sticky=(W))
        config_object.backup_interval_entry = ttk.Entry(main_interval_frame, width=self.entry_width)
        config_object.backup_interval_entry.grid(column=2, row=3, sticky=(W))
        
    
    def config_optional_config_in_main_tab(self):
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
        deleteOldBackupsEntry = ttk.Entry(self.optional_config_frame, width=self.entry_width)
        deleteOldBackupsEntry.grid(column=2, row=4, sticky=(W))
        
    
    def config_server_functions_in_main_tab(self):
        server_functions_frame = LabelFrame(self.main_tab, text="Server Functions")
        server_functions_frame.grid(column=0, row=2, padx=10, pady=10, sticky=(N, W, E, S))

        functions_combobox = ttk.Combobox(server_functions_frame, justify="center", state="readonly", values=["Start Server", "Graceful Shutdown", "Force Shutdown", "Update Server", "Validate Server Files", "Backup Server"])
        functions_combobox.grid(column=0, row=0, padx=10, pady=10)
        functions_combobox.set("-SELECT-")

        functions_go_button = ttk.Button(server_functions_frame, text="Run", command="functions_go_button_click")
        functions_go_button.grid(column=1, row=0)


    def create_output_window(self):
        outputFrame = Frame(self.root)
        outputFrame.pack(side="bottom", expand=True, fill="both")

        outputLabel = ttk.Label(outputFrame, text="Output Window:")
        outputLabel.pack()

        # scrollbar for output window
        scrollbar = ttk.Scrollbar(outputFrame, orient='vertical')
        scrollbar.pack(side="right", fill="y")

        # text widget for the output
        self.output_text = Text(outputFrame, wrap="word", height=10, width=85, yscrollcommand=scrollbar.set)
        self.output_text.pack(padx=10, pady=10, expand=True, fill="both")

        scrollbar.config(command=self.output_text.yview)
    
    
    # Function that sends message to output window
    def append_to_output(self, message):
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        formatted_message = timestamp + message
        self.output_text.insert("end", formatted_message + "\n")
        self.output_text.yview("end")  # Auto-scroll to the bottom
        
    def set_exit_conditions(self):
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def on_closing(self):
        config_object.save_config()
        self.root.destroy()
        
    def start_mainloop(self):
        self.root.mainloop()