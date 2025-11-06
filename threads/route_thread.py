from PyQt6.QtCore import QThread, pyqtSignal
import subprocess

class RouteThread(QThread):
    progress = pyqtSignal(str)

    def __init__(self, dest, gateway, iface, source_ip=""):
        super().__init__()
        self.dest = dest
        self.gateway = gateway
        self.iface = iface
        self.source_ip = source_ip

    def run(self):
        cmd = ["sudo", "ip", "route", "add", self.dest, "via", self.gateway, "dev", self.iface]
        if self.source_ip:
            cmd += ["src", self.source_ip]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                self.progress.emit("Route ajoutée avec succès.")
            else:
                self.progress.emit(f"Erreur : {result.stderr.strip()}")
        except Exception as e:
            self.progress.emit(f"Erreur : {e}")
