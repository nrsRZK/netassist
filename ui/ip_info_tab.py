from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
import socket

class IPInfoTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.label = QLabel("Appuie sur le bouton pour obtenir ton IP locale")
        layout.addWidget(self.label)

        self.btn = QPushButton("Obtenir IP locale")
        self.btn.clicked.connect(self.get_local_ip)
        layout.addWidget(self.btn)

        self.setLayout(layout)

    def get_local_ip(self):
        ip = self.get_ip()
        self.label.setText(f"Ton IP locale est : {ip}")

    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
        except Exception:
            ip = "127.0.0.1"
        finally:
            s.close()
        return ip
