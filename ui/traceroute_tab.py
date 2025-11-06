from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from threads.traceroute_thread import TracerouteThread
from utils.helpers import is_valid_ip, is_valid_domain

class TracerouteTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Entrer IP ou domaine pour traceroute :"))
        self.input = QLineEdit()
        layout.addWidget(self.input)

        self.btn = QPushButton("Lancer Traceroute")
        self.btn.clicked.connect(self.start_traceroute)
        layout.addWidget(self.btn)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def start_traceroute(self):
        target = self.input.text().strip()
        if not target:
            self.output.setPlainText("Veuillez entrer une IP ou un domaine.")
            return
        if not (is_valid_ip(target) or is_valid_domain(target)):
            self.output.setPlainText("IP ou domaine invalide.")
            return
        self.output.clear()
        self.thread = TracerouteThread(target)
        self.thread.progress.connect(self.update_output)
        self.thread.start()

    def update_output(self, text):
        self.output.append(text)
