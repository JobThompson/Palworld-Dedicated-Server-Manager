from Classes.Interface import Interface
from Classes.EmailHandler import EmailHandler
from Classes.Server import Server

def main():
    """Main function that runs the program"""
    email_handler = EmailHandler()
    main_window = Interface(email_handler=email_handler)
    Server("Palworld", main_window)
    main_window.run()


if __name__ == "__main__":
    main()
