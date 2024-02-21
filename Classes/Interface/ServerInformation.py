from customtkinter import CTkFrame, CTkLabel, CTkButton
import tkinter

class ServerInformation(CTkFrame):
    """Class to handle the server information widgets."""
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.label_font = ("Arial", 12, "bold")
    
    def create_server_info(self, form):
        """Create the server information widgets."""
        # Column 0
        server_status = CTkLabel(self, text="Server Status:", fg_color="transparent", font=self.label_font)
        server_status.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        server_version = CTkLabel(self, text="Server Version:", fg_color="transparent", font=self.label_font)
        server_version.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        server_name = CTkLabel(self, text="Name:", fg_color="transparent", font=self.label_font)
        server_name.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")
        server_description = CTkLabel(self, text="Description:", fg_color="transparent", font=self.label_font)
        server_description.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")
        server_password = CTkLabel(self, text="Password:", fg_color="transparent", font=self.label_font)
        server_password.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")
        max_players = CTkLabel(self, text="Max Players:", fg_color="transparent", font=self.label_font)
        max_players.grid(row=5, column=0, padx=10, pady=(10, 0), sticky="w")
        
        # Column 1
        form.server_status = CTkLabel(self, text="server_status", fg_color="transparent")
        form.server_status.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="w")
        form.server_version = CTkLabel(self, text="Server Version:", fg_color="transparent")
        form.server_version.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        form.server_name = CTkLabel(self, text="server_name", fg_color="transparent")
        form.server_name.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="w")
        form.server_description = CTkLabel(self, text="server_description", fg_color="transparent")
        form.server_description.grid(row=3, column=1, padx=10, pady=(10, 0), sticky="w")
        form.server_password = CTkLabel(self, text="server_password", fg_color="transparent")
        form.server_password.grid(row=4, column=1, padx=10, pady=(10, 0), sticky="w")
        form.max_players = CTkLabel(self, text="max_players", fg_color="transparent")
        form.max_players.grid(row=5, column=1, padx=10, pady=(10, 0), sticky="w")
        
        # Column 2
        server_rcon_port = CTkLabel(self, text="RCON Port:", fg_color="transparent", font=self.label_font)
        server_rcon_port.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="w")
        server_rcon_enabled = CTkLabel(self, text="RCON Status:", fg_color="transparent", font=self.label_font)
        server_rcon_enabled.grid(row=1, column=2, padx=10, pady=(10, 0), sticky="w")
        server_rcon_password = CTkLabel(self, text="RCON Password:", fg_color="transparent", font=self.label_font)
        server_rcon_password.grid(row=2, column=2, padx=10, pady=(10, 0), sticky="w")
        
        # Column 3
        form.server_rcon_port = CTkLabel(self, text="server_RCON_port", fg_color="transparent")
        form.server_rcon_port.grid(row=0, column=3, padx=10, pady=(10, 0), sticky="w")
        form.server_rcon_enabled = CTkLabel(self, text="server_RCON_enabled", fg_color="transparent")
        form.server_rcon_enabled.grid(row=1, column=3, padx=10, pady=(10, 0), sticky="w")
        form.server_rcon_password = CTkLabel(self, text="server_RCON_password", fg_color="transparent")
        form.server_rcon_password.grid(row=2, column=3, padx=10, pady=(10, 0), sticky="w")
        
        # Bottom Row
        open_ini_file_button = CTkButton(self, text="Open INI File", command=lambda: self.open_ini_file(form))
        open_ini_file_button.grid(row=6, column=0, columnspan=4, pady=(20, 10), padx=10, sticky="esw")
        
    def open_ini_file(self, form):
        """Open the server's ini file."""
        form.open_modal("Open INI File")
