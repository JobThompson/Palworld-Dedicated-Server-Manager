from customtkinter import CTk
from Classes.Interface.ServerInformation import ServerInformation
from Classes.Interface.ServerConfiguration import ServerConfiguration
from Classes.Interface.ServerFunctions import ServerFunctions
from Classes.Interface.ServerFunctionConfiguration import ServerFunctionConfiguration
from Classes.Interface.OutputWindow import OutputWindow
from Classes.Interface.NotificationConfiguration import NotificationConfiguration
from Classes.Interface.About import About
from Classes.Interface.Tabs import Tabs


class MainWindow(CTk):
    """Main window class. This class is the main window for the program."""
    def __init__(self, form):
        super().__init__()
        self.exit_conditions(form)
        self.iconbitmap('palworld_logo.ico')
        self.title("PalWorld Server Manager - Modern UI")
        self.geometry("900x800")
        self.resizable(True, True)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.create_output_window()
        form.write_output = self.output_window.append_to_output
        self.create_tabed_view()
        self.create_server_info_widgets(form)
        self.create_server_config_widgets(form)
        self.create_server_function_configuration_widgets(form)
        self.create_server_function_widgets(form)
        self.create_notification_configuration_widgets(form)
        self.create_about_widgets(form)
        form.import_config()

    def exit_conditions(self, form):
        """Set the exit conditions for the main window."""
        self.protocol("WM_DELETE_WINDOW", lambda: self.handle_application_close(form))

    def handle_application_close(self, form):
        """Handle the application close event."""
        form.handle_application_close()
        self.destroy()

    def create_output_window(self):
        """Create the output window for the main window."""
        self.output_window = OutputWindow(master=self, width=400, corner_radius=4)
        self.output_window.grid(row=3, column=0, columnspan=4, sticky="nsew")

    def create_tabed_view(self):
        """Create the tabbed view for the main window."""
        self.tabbed_view = Tabs(self)
        self.tabbed_view.grid(row=0, column=0, padx=20, pady=20, sticky="new")

    def create_server_info_widgets(self, form):
        """Create the server information widgets."""
        form.write_output("Creating server information widgets.")
        self.server_info_frame = ServerInformation(master=self.tabbed_view.tab("Server"))
        self.server_info_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="new")
        self.server_info_frame.create_server_info(form)

    def create_server_config_widgets(self, form):
        """Create the server configuration widgets."""
        form.write_output("Creating server configuration widgets.")
        self.server_config_frame = ServerConfiguration(master=self.tabbed_view.tab("Server"))
        self.server_config_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=(0,10), sticky="nwe")
        self.server_config_frame.create_server_configuration(form)

    def create_server_function_widgets(self, form):
        """Create the server function widgets."""
        form.write_output("Creating server function widgets.")
        self.server_function_frame = ServerFunctions(master=self.tabbed_view.tab("Server"))
        self.server_function_frame.grid(row=0, column=4, rowspan=2, padx=10, pady=10, sticky="e")
        self.server_function_frame.create_server_function_widgets(form)

    def create_server_function_configuration_widgets(self, form):
        """Create the server function configuration widgets."""
        form.write_output("Creating server function configuration widgets.")
        self.server_function_configuration_frame = ServerFunctionConfiguration(master=self.tabbed_view.tab("Server"))
        self.server_function_configuration_frame.grid(row=2, column=4, columnspan=1, rowspan=2, padx=10, pady=10, sticky="ne")
        self.server_function_configuration_frame.create_server_function_configuration(form)

    def create_notification_configuration_widgets(self, form):
        """Create the notification configuration widgets."""
        form.write_output("Creating notification configuration widgets.")
        self.notification_configuration_frame = NotificationConfiguration(master=self.tabbed_view.tab("Notification"))
        self.notification_configuration_frame.grid(row=0, column=4, columnspan=1, rowspan=2, padx=10, pady=10, sticky="ne")
        self.notification_configuration_frame.create_notification_configuration(form)

    def create_about_widgets(self, form):
        """Create the about widgets."""
        form.write_output("Creating about widgets.")
        self.about_frame = About(master=self.tabbed_view.tab("About"))
        self.about_frame.grid(row=0, column=0, columnspan=3, rowspan=3, padx=10, pady=10, sticky="nsew")
        self.about_frame.create_about_widgets()

    def run(self):
        """Run the main window."""
        self.mainloop()
