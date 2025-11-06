import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget
from ui.ping_tab import PingTab
from ui.traceroute_tab import TracerouteTab
from ui.ssh_tab import SshTab
from ui.route_tab import RouteTab
from ui.scan_tab import ScanTab

from ui.network_info_tab import NetworkInfoTab
from ui.nmap_tab import NmapTab


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Assistant Réseau Complet")
        self.setGeometry(100, 100, 700, 500)

        self.tabs = QTabWidget()
        self.tabs.addTab(PingTab(), "Ping")
        self.tabs.addTab(TracerouteTab(), "Traceroute")
        self.tabs.addTab(SshTab(), "SSH")
        self.tabs.addTab(RouteTab(), "Config Route")
        self.tabs.addTab(ScanTab(), "Scan Ports")
        
        self.tabs.addTab(NetworkInfoTab(), "Info Réseau")   # Ajout onglet IP locale + passerelle
        self.tabs.addTab(NmapTab(), "Scan Nmap")             # Ajout onglet scan Nmap

        self.setCentralWidget(self.tabs)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
