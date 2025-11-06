from PyQt6.QtCore import QThread, pyqtSignal
import subprocess

class TracerouteThread(QThread):
    progress = pyqtSignal(str)

    def __init__(self, target):
        super().__init__()
        self.target = target

    def run(self):
        cmd = ["traceroute", self.target]
        try:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in iter(process.stdout.readline, ''):
                if line:
                    self.progress.emit(line.strip())
            process.stdout.close()
            process.wait()
        except Exception as e:
            self.progress.emit(f"Erreur traceroute: {e}")
