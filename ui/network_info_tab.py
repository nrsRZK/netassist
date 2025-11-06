from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
import socket
import subprocess

class NetworkInfoTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.ip_label = QLabel("IP locale : -")
        self.gateway_label = QLabel("Passerelle : -")

        self.refresh_btn = QPushButton("Rafraîchir")
        self.refresh_btn.clicked.connect(self.refresh_info)

        layout.addWidget(self.ip_label)
        layout.addWidget(self.gateway_label)
        layout.addWidget(self.refresh_btn)

        self.setLayout(layout)
        self.refresh_info()

    def get_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
        except Exception:
            ip = "127.0.0.1"
        finally:
            s.close()
        return ip

    def get_default_gateway(self):
        try:
            result = subprocess.run(["ip", "route", "show", "default"], capture_output=True, text=True)
            if result.returncode == 0:
                line = result.stdout.strip()
                parts = line.split()
                if "via" in parts:
                    idx = parts.index("via")
                    gateway_ip = parts[idx + 1]
                    return gateway_ip
            return "Passerelle non trouvée"
        except Exception as e:
            return f"Erreur : {e}"

    def refresh_info(self):
        ip = self.get_local_ip()
        gateway = self.get_default_gateway()
        self.ip_label.setText(f"IP locale : {ip}")
        self.gateway_label.setText(f"Passerelle : {gateway}")
