import tkinter
from customtkinter import CTk, CTkButton, CTkFrame, set_appearance_mode
from Classes.Interface.ServerInformation import ServerInformation
from Classes.Interface.ServerConfiguration import ServerConfiguration
from Classes.Interface.ServerFunctions import ServerFunctions


class MainWindow(CTk):
    """Main window class. This class is the main window for the program."""
    def __init__(self, form):
        super().__init__()
        self.iconbitmap('palworld_logo.ico')
        self.title("PalWorld Server Manager - Modern UI")
        self.geometry("800x600")
        self.resizable(True, True)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.create_server_info_widgets(form)
        self.create_server_config_widgets(form)
        self.create_server_function_widgets(form)
        
        
    def create_server_info_widgets(self, form):
        self.server_info_frame = ServerInformation(master=self)
        self.server_info_frame.create_server_info(form)
        
    def create_server_config_widgets(self, form):
        self.server_config_frame = ServerConfiguration(master=self)
        self.server_config_frame.create_server_configuration(form)
        
    def create_server_function_widgets(self, form):
        self.server_function_frame = ServerFunctions(master=self)
        self.server_function_frame.create_server_function_widgets(form)
        
    def run(self):
        self.mainloop()