from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt6.QtCore import Qt
from threads.ping_thread import PingThread
from utils.helpers import is_valid_ip, is_valid_domain
from config import PING_COUNT

class PingTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Entrer IP ou domaine à pinguer :"))
        self.ip_input = QLineEdit()
        layout.addWidget(self.ip_input)

        self.ping_btn = QPushButton("Lancer Ping")
        self.ping_btn.clicked.connect(self.start_ping)
        layout.addWidget(self.ping_btn)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def start_ping(self):
        target = self.ip_input.text().strip()
        if not target:
            self.output.setPlainText("Veuillez entrer une IP ou un domaine.")
            return
        if not (is_valid_ip(target) or is_valid_domain(target)):
            self.output.setPlainText("IP ou domaine invalide.")
            return
        self.output.clear()
        self.thread = PingThread(target, count=PING_COUNT)
        self.thread.progress.connect(self.update_output)
        self.thread.start()

    def update_output(self, text):
        self.output.append(text)
