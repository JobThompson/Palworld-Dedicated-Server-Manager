from Classes.Interface import Interface
from Classes.EmailHandler import EmailHandler

def main():
    """Main function that runs the program"""
    email_handler = EmailHandler()
    main_window = Interface(email_handler=email_handler)
    main_window.run()


if __name__ == "__main__":
    main()
