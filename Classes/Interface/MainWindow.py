from customtkinter import CTk, CTkTextbox
from Classes.Interface.ServerInformation import ServerInformation
from Classes.Interface.ServerConfiguration import ServerConfiguration
from Classes.Interface.ServerFunctions import ServerFunctions
from Classes.Interface.OutputWindow import OutputWindow
from Classes.Interface.Tabs import Tabs


class MainWindow(CTk):
    """Main window class. This class is the main window for the program."""
    def __init__(self, form):
        super().__init__()
        self.iconbitmap('palworld_logo.ico')
        self.title("PalWorld Server Manager - Modern UI")
        self.geometry("800x800")
        self.resizable(True, True)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.create_output_window()
        form.write_output = self.output_window.append_to_output
        self.create_tabed_view()
        self.create_server_info_widgets(form)
        self.create_server_config_widgets(form)
        self.create_server_function_widgets(form)
        
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
        self.server_info_frame.grid(row=0, column=0, columnspan=3, padx=20, pady=10, sticky="new")
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
        self.server_function_frame.grid(row=0, column=4, columnspan=1, rowspan=2, padx=20, pady=10, sticky="ne")
        self.server_function_frame.create_server_function_widgets(form)
        
    def run(self):
        self.mainloop()