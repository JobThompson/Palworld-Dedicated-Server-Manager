class Server:
    """Server class to store server information and operate on server data"""
    def __init__(self, name, ip, port):
        self.name = name
        self.ip = ip
        self.port = port
        self.status = "offline"
