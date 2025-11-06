from PyQt6.QtWidgets import QWidget, QFormLayout, QLineEdit, QPushButton, QTextEdit
from threads.route_thread import RouteThread

class RouteTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QFormLayout()

        self.dest_input = QLineEdit()
        self.gateway_input = QLineEdit()
        self.iface_input = QLineEdit()
        self.source_ip_input = QLineEdit()  # Nouveau champ optionnel

        layout.addRow("Destination (ex: 192.168.1.0/24) :", self.dest_input)
        layout.addRow("Passerelle (Gateway) :", self.gateway_input)
        layout.addRow("Interface (ex: eth0) :", self.iface_input)
        layout.addRow("IP source (optionnelle) :", self.source_ip_input)  # Ajout au formulaire

        self.add_route_btn = QPushButton("Ajouter la route")
        self.add_route_btn.clicked.connect(self.add_route)
        layout.addRow(self.add_route_btn)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addRow(self.output)

        self.setLayout(layout)

    def add_route(self):
        dest = self.dest_input.text().strip()
        gateway = self.gateway_input.text().strip()
        iface = self.iface_input.text().strip()
        source_ip = self.source_ip_input.text().strip()

        if not all([dest, gateway, iface]):
            self.output.setPlainText("Merci de remplir les champs Destination, Passerelle et Interface.")
            return

        self.output.clear()
        # Passe aussi source_ip (vide si non renseigné)
        self.thread = RouteThread(dest, gateway, iface, source_ip)
        self.thread.progress.connect(self.update_output)
        self.thread.start()

    def update_output(self, text):
        self.output.append(text)
