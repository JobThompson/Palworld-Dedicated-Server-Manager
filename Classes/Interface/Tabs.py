from customtkinter import CTkTabview

class Tabs(CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.anchor = "nw"
        self.width = 200
        self.height = 40
        self.add("Server")
        self.add("Notification")
        self.add("Backup")
        self.add("About")