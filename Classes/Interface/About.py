from customtkinter import CTkFrame, CTkLabel, CTkButton

class About(CTkFrame):
    """Class to handle the notification configuration widgets."""
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.label_font = ("Arial", 12, "bold")
        
    def create_about_widgets(self):
        """Create the about widgets."""
        # Column 0
        app_version_label = CTkLabel(self, text="App Version:", fg_color="transparent", font=self.label_font)
        app_version_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        
        app_author_label = CTkLabel(self, text="App Author:", fg_color="transparent", font=self.label_font)
        app_author_label.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        
        app_github_label = CTkLabel(self, text="App Github:", fg_color="transparent", font=self.label_font)
        app_github_label.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")
        
        feedback_label = CTkLabel(self, text="Have feedback or suggestions? Discord:", fg_color="transparent", font=self.label_font)
        feedback_label.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")
        
        buy_me_a_coffee_label = CTkLabel(self, text="Consider buying me a coffee:", fg_color="transparent", font=self.label_font)
        buy_me_a_coffee_label.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")


        # Column 1
        app_version = CTkLabel(self, text="1.0.0", fg_color="transparent")
        app_version.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="w")
        
        app_author = CTkLabel(self, text="Andrew1175", fg_color="transparent")
        app_author.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="w")
        
        app_github = CTkLabel(self, text="https://github.com/Andrew1175/Palworld-Dedicated-Server-Manager", fg_color="transparent", cursor="hand2")
        app_github.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="w")
        
        discord_link = CTkLabel(self, text="https://discord.gg/bPp9kfWe5t", fg_color="transparent",  cursor="hand2")
        discord_link.grid(row=3, column=1, padx=10, pady=(10, 0), sticky="w")
        
        buy_me_a_coffee_value = CTkLabel(self, text="https://www.buymeacoffee.com/thewisestguy", fg_color="transparent", cursor="hand2")
        buy_me_a_coffee_value.grid(row=4, column=1, padx=10, pady=(10, 0), sticky="w")


        # Column 2
        app_update_button = CTkButton(self, text="Check for Updates", command=self.check_for_updates)
        app_update_button.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="esw")
        
        app_report_bug_button = CTkButton(self, text="Report a Bug", command=self.report_bug)
        app_report_bug_button.grid(row=1, column=2, padx=10, pady=(10, 0), sticky="esw")


        # Bottom Row
        app_supporters_label = CTkLabel(self, text="App Supporters: daisame.bsky.social, CBesty", fg_color="transparent", font=self.label_font)
        app_supporters_label.grid(row=5, column=0, padx=10, pady=(10, 0), sticky="swe")
        
    def check_for_updates(self):
        pass
    
    def report_bug(self):
        pass