from Classes.Interface import Interface
from Classes.EmailHandler import EmailHandler
from Classes.Server import Server

def main():
    """Main function that runs the program"""
    main_window = Interface( server=Server("Palworld"), email_handler=EmailHandler())
    main_window.run()


if __name__ == "__main__":
    main()
