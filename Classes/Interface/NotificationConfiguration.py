from customtkinter import CTkFrame

class NotificationConfiguration(CTkFrame):
    """Class to handle the notification configuration widgets."""
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.label_font = ("Arial", 12, "bold")
