from customtkinter import CTkFrame, set_appearance_mode

class ThemeConfiguration(CTkFrame):
    """Class to handle the notification configuration widgets."""
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.label_font = ("Arial", 12, "bold")
        
    def set_light_mode(self):
        """Set the theme to light mode."""
        set_appearance_mode("Light")
        
    def set_dark_mode(self):
        """Set the theme to dark mode."""
        set_appearance_mode("Dark")

