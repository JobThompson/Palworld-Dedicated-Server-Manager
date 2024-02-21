from Classes.Interface.MainWindow import MainWindow
from Classes.Form import Form

def main():
    """Main function that runs the program"""
    form = Form()
    interface_instance = MainWindow(form)
    interface_instance.run()

if __name__ == "__main__":
    main()
    