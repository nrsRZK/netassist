from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt6.QtCore import QThread, pyqtSignal
import subprocess

class NmapThread(QThread):
    result_ready = pyqtSignal(str)

    def __init__(self, target):
        super().__init__()
        self.target = target

    def run(self):
        try:
            result = subprocess.run(["nmap", "-sV", self.target], capture_output=True, text=True)
            self.result_ready.emit(result.stdout)
        except Exception as e:
            self.result_ready.emit(f"Erreur : {e}")

class NmapTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.label = QLabel("Cible à scanner (IP ou domaine) :")
        layout.addWidget(self.label)

        self.target_input = QLineEdit()
        layout.addWidget(self.target_input)

        self.scan_btn = QPushButton("Lancer le scan Nmap")
        self.scan_btn.clicked.connect(self.start_scan)
        layout.addWidget(self.scan_btn)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def start_scan(self):
        target = self.target_input.text().strip()
        if not target:
            self.output.setPlainText("Merci d'entrer une cible valide.")
            return

        self.output.clear()
        self.scan_btn.setEnabled(False)
        self.thread = NmapThread(target)
        self.thread.result_ready.connect(self.show_result)
        self.thread.start()

    def show_result(self, result):
        self.output.setPlainText(result)
        self.scan_btn.setEnabled(True)
