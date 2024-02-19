from tkinter import TclError, Tk, ttk, N, W, E, S, StringVar, LabelFrame, BooleanVar, Frame, Text
from Classes.Config import config_object
from Classes.Form import form
from Classes.DiscordHandler import discord_handler

class Interface:
    """Class that handles the TKinter interface for the server manager"""
    def __init__(self, server, email_handler) -> None:
        self.email_handler = email_handler
        self.server = server

        self.root = Tk()
        self.mainframe = None
        self.tab_control = None

        self.entry_width = 10
        
        self.create_output_window() # This goes first so that the output window is created before any output is sent to it.
        
        self.set_favicon('palworld_logo.ico')
        self.configure_main_window_size()
        self.create_tabs()
        self.config_interval_configuration_in_main_tab()
        self.config_optional_config_in_main_tab()
        self.config_server_functions_in_main_tab()
        self.config_server_info_in_main_tab()
        self.config_palworld_ini_in_server_config_tab()
        self.configure_server_configuration_in_server_configure_tab()
        self.configure_email_configuration_in_alerts_tab()
        self.configure_discord_configuration_in_alerts_tab()
        self.configure_about_tab()
        self.set_exit_conditions()
        config_object.load_config()

 
    def set_favicon(self, icon_path):
        """Sets the favicon for the main window"""
        try:
            self.root.iconbitmap(icon_path)
            form.append_to_output("Icon loaded successfully.")
        except FileNotFoundError as e:
            form.append_to_output("Icon file not found: " + str(e))
        except TclError as e:
            form.append_to_output("Error loading icon: " + str(e))


    def configure_main_window_size(self):
        """Configures the main window size and title"""
        self.root.title("PalWorld Server Manager")
        self.root.geometry("800x600")
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")


    def create_tabs(self):
        """Creates the tabs for the interface"""
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


    """ Main Tab Configuration """
    def config_interval_configuration_in_main_tab(self):
        """Configures the interval configuration section of the main tab"""
        main_interval_frame = LabelFrame(self.main_tab, text="Interval Configuration")
        main_interval_frame.grid(column=0, row=0, padx=10, pady=10, sticky=(N, W, E, S))
        form.restart_interval_checkbox_var = BooleanVar()
        restart_interval_checkbox = ttk.Checkbutton(
            main_interval_frame,
            variable=form.restart_interval_checkbox_var,
            command="enable_server_restart"
        )
        restart_interval_checkbox.grid(column=0, row=0)
        restart_label = ttk.Label(
            main_interval_frame,
            text="Server Restart Interval (hours):"
        )
        restart_label.grid(column=1, row=0, sticky=W)
        form.restart_entry = ttk.Entry(main_interval_frame, width=self.entry_width)
        form.restart_entry.grid(column=2, row=0, sticky=W)

        form.restart_schedule_checkbox_var = BooleanVar()
        restart_schedule_checkbox = ttk.Checkbutton(
            main_interval_frame,
            variable=form.restart_schedule_checkbox_var,
            command="enable_scheduled_restart"
        )
        restart_schedule_checkbox.grid(column=0, row=1)
        restart_schedule_label = ttk.Label(
            main_interval_frame,
            text="Daily Server Restart Time (12-hour Format):"
        )
        restart_schedule_label.grid(column=1, row=1, sticky=W)
        form.restart_schedule_entry_var = StringVar()
        form.restart_schedule_entry = ttk.Entry(
            main_interval_frame,
            textvariable=form.restart_schedule_entry_var,
            width=self.entry_width
        )
        form.restart_schedule_entry.grid(column=2, row=1, sticky=W)
        form.ampm_var = StringVar(value="AM")
        ampm_combobox = ttk.Combobox(
            main_interval_frame,
            textvariable=form.ampm_var,
            values=["AM", "PM"],
            width=4
        )
        ampm_combobox.grid(column=3, row=1)

        form.monitor_interval_checkbox_var = BooleanVar()
        monitor_interval_checkbox = ttk.Checkbutton(
            main_interval_frame,
            variable=form.monitor_interval_checkbox_var,
            command="enable_monitor_server"
        )
        monitor_interval_checkbox.grid(column=0, row=2)
        monitor_label = ttk.Label(main_interval_frame, text="Monitor Interval (minutes):")
        monitor_label.grid(
            column=1,
            row=2,
            sticky=W
        )
        form.monitor_entry = ttk.Entry(main_interval_frame, width=self.entry_width)
        form.monitor_entry.grid(column=2, row=2, sticky=W)

        form.backup_interval_checkbox_var = BooleanVar()
        backup_interval_checkbox = ttk.Checkbutton(
            main_interval_frame,
            variable=form.backup_interval_checkbox_var,
            command="enable_backup_interval"
        )
        backup_interval_checkbox.grid(column=0, row=3)
        backup_interval_label = ttk.Label(
            main_interval_frame,
            text="Backup Server Interval (hours):"
        )
        backup_interval_label.grid(column=1, row=3, sticky=W)
        form.backup_interval_entry = ttk.Entry(main_interval_frame, width=self.entry_width)
        form.backup_interval_entry.grid(column=2, row=3, sticky=W)


    def config_optional_config_in_main_tab(self):
        """Configures the optional configurations section of the main tab"""
        self.optional_config_frame = LabelFrame(self.main_tab, text="Optional Configurations")
        self.optional_config_frame.grid(column=0, row=1, padx=10, pady=10, sticky=(N, W, E, S))

        form.send_email_checkbox_var = BooleanVar()
        send_email_checkbox = ttk.Checkbutton(
            self.optional_config_frame,
            variable=form.send_email_checkbox_var,
            command="enable_send_email"
        )
        send_email_checkbox.grid(column=0, row=0)
        send_email_label = ttk.Label(
            self.optional_config_frame,
            text="Send Notification Email on crash"
        )
        send_email_label.grid(column=1, row=0, sticky=W)

        form.discord_webhook_checkbox_var = BooleanVar()
        discord_webhook_checkbox = ttk.Checkbutton(
            self.optional_config_frame,
            variable=form.discord_webhook_checkbox_var,
            command="enable_send_discord_message"
        )
        discord_webhook_checkbox.grid(column=0, row=1)
        discord_webhook_label = ttk.Label(
            self.optional_config_frame,
            text="Send Discord channel message on crash"
        )
        discord_webhook_label.grid(column=1, row=1, sticky=W)

        form.update_server_startup_checkbox_var = BooleanVar()
        update_server_startup_checkbox = ttk.Checkbutton(
            self.optional_config_frame,
            variable=form.update_server_startup_checkbox_var,
            command="enable_server_updates_on_startup"
        )
        update_server_startup_checkbox.grid(column=0, row=2)
        update_server_startup_label = ttk.Label(
            self.optional_config_frame,
            text="Check for updates on startup"
        )
        update_server_startup_label.grid(column=1, row=2, sticky=W)

        form.backup_server_checkbox_var = BooleanVar()
        backup_server_checkbox = ttk.Checkbutton(
            self.optional_config_frame,
            variable=form.backup_server_checkbox_var,
            command="enable_server_backups"
        )
        backup_server_checkbox.grid(column=0, row=3)
        backup_server_label = ttk.Label(
            self.optional_config_frame,
            text="Backup server during restarts"
        )
        backup_server_label.grid(column=1, row=3, sticky=W)

        form.delete_old_backups_checkbox_var = BooleanVar()
        delete_old_backups_checkbox = ttk.Checkbutton(
            self.optional_config_frame,
            variable=form.delete_old_backups_checkbox_var,
            command="enable_delete_backups"
        )
        delete_old_backups_checkbox.grid(column=0, row=4)
        delete_old_backups_label = ttk.Label(
            self.optional_config_frame,
            text="Delete Backups Older Than (Days):"
        )
        delete_old_backups_label.grid(column=1, row=4, sticky=W)
        form.delete_old_backups_entry = ttk.Entry(self.optional_config_frame, width=self.entry_width)
        form.delete_old_backups_entry.grid(column=2, row=4, sticky=W)


    def config_server_functions_in_main_tab(self):
        """Configures the server functions section of the main tab"""
        server_functions_frame = LabelFrame(self.main_tab, text="Server Functions")
        server_functions_frame.grid(column=0, row=2, padx=10, pady=10, sticky=(N, W, E, S))

        functions_combobox = ttk.Combobox(
            server_functions_frame,
            justify="center",
            state="readonly",
            values=[
                "Start Server", 
                "Graceful Shutdown", 
                "Force Shutdown", 
                "Update Server", 
                "Validate Server Files", 
                "Backup Server"
            ])
        functions_combobox.grid(column=0, row=0, padx=10, pady=10)
        functions_combobox.set("-SELECT-")

        functions_go_button = ttk.Button(
            server_functions_frame,
            text="Run",
            command="functions_go_button_click"
        )
        functions_go_button.grid(column=1, row=0)


    def config_server_info_in_main_tab(self):
        """Configures the server information section of the main tab"""
        server_info_frame = LabelFrame(self.main_tab, text="Server Information")
        server_info_frame.grid(column=1, row=0, padx=10, pady=10, sticky=(N, W, E, S))

        server_status_label = ttk.Label(server_info_frame, text="Server Status:")
        server_status_label.grid(column=0, row=0, sticky=W)

        server_status_state_label = ttk.Label(server_info_frame, text="-")
        server_status_state_label.grid(column=1, row=0)

        server_version_label = ttk.Label(server_info_frame, text="Server Version:")
        server_version_label.grid(column=0, row=1, sticky=W)

        server_version_state_label = ttk.Label(server_info_frame, text="-")
        server_version_state_label.grid(column=1, row=1)

        update_info_button = ttk.Button(
            server_info_frame,
            text="Update Now",
            command="server_status_info"
        )
        update_info_button.grid(column=0, row=3, columnspan=2, sticky=N)
        
    """ Server Config Tab Configuration """
    def config_palworld_ini_in_server_config_tab(self):
        """Configures the PalWorldSettings.ini section of the server config tab"""
        server_info_frame = LabelFrame(self.server_config_tab, text="PalWorldSettings.ini")
        server_info_frame.grid(column=0, row=0, padx=10, pady=10)

        form.server_name_label = ttk.Label(server_info_frame, text="Server Name:")
        form.server_name_label.grid(column=0, row=0, sticky=W, padx=10)

        form.server_name = ttk.Label(server_info_frame, text="-")
        form.server_name.grid(column=0, row=1, sticky=W, padx=10)

        form.server_description_label = ttk.Label(server_info_frame, text="Server Description:")
        form.server_description_label.grid(column=0, row=2, sticky=W, padx=10)

        form.server_description = ttk.Label(server_info_frame, text="-")
        form.server_description.grid(column=0, row=3, sticky=W, padx=10)

        form.server_password_label = ttk.Label(server_info_frame, text="Server Password:")
        form.server_password_label.grid(column=0, row=4, sticky=W, padx=10)

        form.server_password = ttk.Label(server_info_frame, text="-")
        form.server_password.grid(column=0, row=5, sticky=W, padx=10)

        form.max_players_label = ttk.Label(server_info_frame, text="Max Players:")
        form.max_players_label.grid(column=1, row=0, sticky=W, padx=10)

        form.max_players = ttk.Label(server_info_frame, text="-")
        form.max_players.grid(column=1, row=1, sticky=W, padx=10)

        form.server_port_label = ttk.Label(server_info_frame, text="Server Port:")
        form.server_port_label.grid(column=1, row=2, sticky=W, padx=10)

        form.server_port = ttk.Label(server_info_frame, text="-")
        form.server_port.grid(column=1, row=3, sticky=W, padx=10)

        form.rcon_port_label = ttk.Label(server_info_frame, text="RCON Port:")
        form.rcon_port_label.grid(column=2, row=0, sticky=W, padx=10)

        form.rcon_port = ttk.Label(server_info_frame, text="-")
        form.rcon_port.grid(column=2, row=1, sticky=W, padx=10)

        form.rcon_state_label = ttk.Label(server_info_frame, text="RCON Enabled:")
        form.rcon_state_label.grid(column=2, row=2, sticky=W, padx=10)

        form.rcon_state = ttk.Label(server_info_frame, text="-")
        form.rcon_state.grid(column=2, row=3, sticky=W, padx=10)

        form.rcon_password_label = ttk.Label(server_info_frame, text="RCON Password:")
        form.rcon_password_label.grid(column=2, row=4, sticky=W, padx=10)

        form.rcon_password = ttk.Label(server_info_frame, text="-")
        form.rcon_password.grid(column=2, row=5, sticky=W, padx=10)

        edit_server_config_button = ttk.Button(
            server_info_frame, 
            text="Edit PalWorldSettings.ini",
            command=lambda: form.open_ini_file(form.server_directory_selection.cget('text'))
        )
        edit_server_config_button.grid(column=0, row=6, columnspan=3, padx=10, pady=10)
    
    def configure_server_configuration_in_server_configure_tab(self):
        """Configures the server configuration section of the server config tab"""
        server_config_frame = LabelFrame(self.server_config_tab, text="Server Configuration")
        server_config_frame.grid(column=0, row=1, padx=10, pady=10)

        server_directory_button = ttk.Button(server_config_frame, text="Select Palworld Directory:", command=self.server.select_palworld_directory)
        server_directory_button.grid(column=0, row=0, padx=10, pady=10)

        form.server_directory_selection = ttk.Label(server_config_frame, text="No directory selected")
        form.server_directory_selection.grid(column=1, row=0, sticky=W)

        form.palworld_exe_result_label = ttk.Label(server_config_frame)
        form.palworld_exe_result_label.grid(column=2, row=0)

        arrcon_directory_button = ttk.Button(server_config_frame, text="Select ARRCON Directory:", command=self.server.select_arrcon_directory)
        arrcon_directory_button.grid(column=0, row=1, padx=10, pady=10)

        form.arrcon_directory_selection = ttk.Label(server_config_frame, text="No directory selected")
        form.arrcon_directory_selection.grid(column=1, row=1, sticky=W)

        form.arrcon_exe_result_label = ttk.Label(server_config_frame)
        form.arrcon_exe_result_label.grid(column=2, row=1)

        steamcmd_directory_button = ttk.Button(server_config_frame, text="Select steamcmd Directory:", command=self.server.select_steamcmd_directory)
        steamcmd_directory_button.grid(column=0, row=2, padx=10, pady=10)

        form.steamcmd_directory_selection = ttk.Label(server_config_frame, text="No directory selected")
        form.steamcmd_directory_selection.grid(column=1, row=2, sticky=W)

        form.steamcmd_exe_result_label = ttk.Label(server_config_frame)
        form.steamcmd_exe_result_label.grid(column=2, row=2)

        backup_directory_button = ttk.Button(server_config_frame, text="Select Backup Directory:", command=self.server.select_backup_directory)
        backup_directory_button.grid(column=0, row=3, padx=10, pady=10)

        form.backup_directory_selection = ttk.Label(server_config_frame, text="No directory selected")
        form.backup_directory_selection.grid(column=1, row=3, sticky=W)

        server_start_args_label = ttk.Label(server_config_frame, text="Server Startup Arguments:")
        server_start_args_label.grid(column=0, row=4, padx=10, pady=10)

        form.server_start_args_entry = ttk.Entry(server_config_frame, width=100)
        form.server_start_args_entry.grid(column=1, row=4, columnspan=2, sticky=W)


    """ Alert Tab Configuration """
    def configure_email_configuration_in_alerts_tab(self):
        """Configures the email configuration section of the alerts tab"""
        email_config_frame = LabelFrame(self.alerts_config_tab, text="Email Configuration")
        email_config_frame.grid(column=0, row=0, padx=10, pady=10, sticky=(N, W, E, S))

        email_address_label = ttk.Label(email_config_frame, text="Email Address:")
        email_address_label.grid(column=0, row=0, padx=10, sticky=W)

        form.email_address_entry = ttk.Entry(email_config_frame, width=35)
        form.email_address_entry.grid(column=1, row=0, sticky=W)

        email_password_label = ttk.Label(email_config_frame, text="Email Password:")
        email_password_label.grid(column=0, row=1, padx=10, sticky=W)

        form.email_password_entry = ttk.Entry(email_config_frame, show="*", width=35)
        form.email_password_entry.grid(column=1, row=1, sticky=W)

        smtp_server_label = ttk.Label(email_config_frame, text="SMTP Server:")
        smtp_server_label.grid(column=0, row=2, padx=10, sticky=W)

        form.smtp_server_entry = ttk.Entry(email_config_frame)
        form.smtp_server_entry.grid(column=1, row=2, sticky=W)

        smtp_port_label = ttk.Label(email_config_frame, text="SMTP Port:")
        smtp_port_label.grid(column=0, row=3, padx=10, sticky=W)

        form.smtp_port_entry = ttk.Entry(email_config_frame, width=5)
        form.smtp_port_entry.grid(column=1, row=3, sticky=W)

    def configure_discord_configuration_in_alerts_tab(self):
        """Configures the discord configuration section of the alerts tab"""
        discord_frame = LabelFrame(self.alerts_config_tab, text="Discord Configuration")
        discord_frame.grid(column=1, row=0, padx=10, pady=10, sticky=(N, W, E, S))

        discord_label = ttk.Label(discord_frame, text="Discord Webhook URL:")
        discord_label.grid(column=0, row=0, padx=10)

        form.discord_entry = ttk.Entry(discord_frame, width=35)
        form.discord_entry.grid(column=1, row=0)

        discord_test_button = ttk.Button(discord_frame, text="Send Test Message", command=discord_handler.post_discord_message)
        discord_test_button.grid(column=0, row=1, columnspan=2, pady=2)

    """ About Tab Configuration """
    def configure_about_tab(self):
        """Configures the about tab"""
        app_info_frame = LabelFrame(self.about_tab, text="Application Info")
        app_info_frame.grid(column=0, row=0, padx=10, pady=10, sticky=N)

        app_version_label = ttk.Label(app_info_frame, text="Application Version: 1.3.0")
        app_version_label.grid(column=0, row=0, padx=10)

        app_update_button = ttk.Button(app_info_frame, text="Check for Updates", command="check_for_updates")
        app_update_button.grid(column=0, row=1, padx=10, pady=10)

        report_bug_button = ttk.Button(app_info_frame, text="Report a Bug", command="report_bug")
        report_bug_button.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

        support_frame = LabelFrame(self.about_tab, text="Support Info")
        support_frame.grid(column=0, row=1, padx=10, pady=10, sticky=(E, W))

        feedback_label = ttk.Label(support_frame, text="Have feedback or suggestions? Join my discord and let me know:")
        feedback_label.grid(column=0, row=0, sticky=E)

        feedback_label_link = ttk.Label(
            support_frame,
            text="https://discord.gg/bPp9kfWe5t",
            foreground="blue",
            cursor="hand2"
        )
        feedback_label_link.grid(column=1, row=0, sticky=W)
        feedback_label_link.bind("<Button-1>", "open_discord")

        buy_me_beer_label = ttk.Label(
            support_frame,
            justify="center",
            text="This application is completely free and no features will ever be behind a paywall. If you would like to support me I would greatly appreciate it. You can buy me a beer here:"
        )
        buy_me_beer_label.grid(column=0, row=1, columnspan=2, sticky=(N, S, E, W))

        buy_me_beer_link = ttk.Label(
            support_frame,
            text="https://www.buymeacoffee.com/thewisestguy",
            foreground="blue",
            cursor="hand2"
        )
        buy_me_beer_link.grid(column=0, row=2, columnspan=2)
        buy_me_beer_link.bind("<Button-1>", "open_BMAB")

        supporters_frame = LabelFrame(self.about_tab, text="Special Thanks to the Following Supporters:")
        supporters_frame.grid(column=0, row=2, padx=10, pady=10, sticky=(E, W))
        supporters_frame.columnconfigure(0, weight=1)

        donations_label = ttk.Label(supporters_frame, justify="center", text="daisame.bsky.social, CBesty")
        donations_label.grid(column=0, row=0)


    """ Output Configuration """
    def create_output_window(self):
        """Creates the output console for the interface"""
        output_frame = Frame(self.root)
        output_frame.pack(side="bottom", expand=True, fill="both", anchor="n")

        output_label = ttk.Label(output_frame, text="Output Window:")
        output_label.pack()

        # scrollbar for output window
        scrollbar = ttk.Scrollbar(output_frame, orient='vertical')
        scrollbar.pack(side="right", fill="y")

        # text widget for the output
        form.output_text = Text(
            output_frame,
            wrap="word",
            height=10,
            width=85,
            yscrollcommand=scrollbar.set
        )
        form.output_text.pack(padx=10, pady=10, expand=True, fill="both")

        scrollbar.config(command=form.output_text.yview)


    def set_exit_conditions(self):
        """Sets the exit conditions for the root window"""
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        """Handles the closing of the window and saves the config file before closing the window"""
        try:
            config_object.save_config()
        except IOError as e:
            form.append_to_output("Error saving config file: " + str(e))
        
        self.root.destroy()

    def run(self):
        """Starts the main loop for the interface"""
        self.root.mainloop()
