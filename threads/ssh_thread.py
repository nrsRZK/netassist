from PyQt6.QtCore import QThread, pyqtSignal
import paramiko

class SshThread(QThread):
    progress = pyqtSignal(str)

    def __init__(self, host, port, user, password, command):
        super().__init__()
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.command = command

    def run(self):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self.host, port=self.port, username=self.user, password=self.password, timeout=10)
            stdin, stdout, stderr = client.exec_command(self.command)
            out = stdout.read().decode()
            err = stderr.read().decode()
            client.close()
            if out:
                self.progress.emit(out)
            if err:
                self.progress.emit(f"Erreur: {err}")
            if not out and not err:
                self.progress.emit("Commande exécutée, mais sans retour.")
        except Exception as e:
            self.progress.emit(f"Erreur SSH: {e}")
