from PyQt6.QtCore import QThread, pyqtSignal
import subprocess

class PingThread(QThread):
    progress = pyqtSignal(str)

    def __init__(self, target, count=4):
        super().__init__()
        self.target = target
        self.count = count

    def run(self):
        cmd = ["ping", "-c", str(self.count), self.target]
        try:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in iter(process.stdout.readline, ''):
                if line:
                    self.progress.emit(line.strip())
            process.stdout.close()
            process.wait()
        except Exception as e:
            self.progress.emit(f"Erreur ping: {e}")
