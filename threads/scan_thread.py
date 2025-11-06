from PyQt6.QtCore import QThread, pyqtSignal
import socket

class ScanThread(QThread):
    progress = pyqtSignal(str)

    def __init__(self, host, start_port, end_port):
        super().__init__()
        self.host = host
        self.start_port = start_port
        self.end_port = end_port

    def run(self):
        for port in range(self.start_port, self.end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((self.host, port))
            if result == 0:
                self.progress.emit(f"Port {port} ouvert")
            sock.close()
        self.progress.emit("Scan terminé.")
