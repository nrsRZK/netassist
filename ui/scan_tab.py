from PyQt6.QtWidgets import QWidget, QFormLayout, QLineEdit, QPushButton, QTextEdit
from threads.scan_thread import ScanThread

class ScanTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QFormLayout()

        self.host_input = QLineEdit()
        self.start_port_input = QLineEdit()
        self.end_port_input = QLineEdit()

        layout.addRow("Hôte :", self.host_input)
        layout.addRow("Port début :", self.start_port_input)
        layout.addRow("Port fin :", self.end_port_input)

        self.scan_btn = QPushButton("Lancer Scan")
        self.scan_btn.clicked.connect(self.start_scan)
        layout.addRow(self.scan_btn)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addRow(self.output)

        self.setLayout(layout)

    def start_scan(self):
        host = self.host_input.text().strip()
        try:
            start_port = int(self.start_port_input.text())
            end_port = int(self.end_port_input.text())
        except ValueError:
            self.output.setPlainText("Les ports doivent être des nombres entiers.")
            return

        if not host:
            self.output.setPlainText("Veuillez entrer une IP ou un domaine.")
            return

        if start_port > end_port:
            self.output.setPlainText("Le port début doit être inférieur ou égal au port fin.")
            return

        self.output.clear()
        self.thread = ScanThread(host, start_port, end_port)
        self.thread.progress.connect(self.update_output)
        self.thread.start()

    def update_output(self, text):
        self.output.append(text)
