from PyQt6.QtWidgets import QWidget, QFormLayout, QLineEdit, QPushButton, QTextEdit
from threads.ssh_thread import SshThread

class SshTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QFormLayout()

        self.host_input = QLineEdit()
        self.port_input = QLineEdit()
        self.port_input.setText("22")
        self.user_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.command_input = QLineEdit()

        layout.addRow("Hôte SSH :", self.host_input)
        layout.addRow("Port :", self.port_input)
        layout.addRow("Utilisateur :", self.user_input)
        layout.addRow("Mot de passe :", self.password_input)
        layout.addRow("Commande :", self.command_input)

        self.ssh_btn = QPushButton("Exécuter")
        self.ssh_btn.clicked.connect(self.run_ssh_command)
        layout.addRow(self.ssh_btn)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addRow(self.output)

        self.setLayout(layout)

    def run_ssh_command(self):
        host = self.host_input.text().strip()
        port = self.port_input.text().strip()
        user = self.user_input.text().strip()
        password = self.password_input.text()
        command = self.command_input.text().strip()

        if not all([host, port, user, password, command]):
            self.output.setPlainText("Merci de remplir tous les champs.")
            return

        try:
            port = int(port)
        except ValueError:
            self.output.setPlainText("Le port doit être un nombre entier.")
            return

        self.output.clear()
        self.thread = SshThread(host, port, user, password, command)
        self.thread.progress.connect(self.update_output)
        self.thread.start()

    def update_output(self, text):
        self.output.append(text)
