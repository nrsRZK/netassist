# 🛰️ NetAssist – Assistant Graphique Réseau pour Linux

> **NetAssist** est une application graphique (GUI) développée en **Python (PyQt6)** pour administrer et diagnostiquer facilement un réseau Linux.  
> Elle centralise des outils comme **ping**, **traceroute**, **SSH**, **nmap**, et **tshark**, le tout dans une interface simple et moderne.

---

## 🚀 Fonctionnalités principales

- 📡 **Ping & Traceroute** — Teste la connectivité réseau.
- 🔐 **SSH Manager** — Connexion à distance aux serveurs Linux via Paramiko.
- 🌍 **Scan de ports (Nmap)** — Détection des services ouverts sur un hôte.
- 🧭 **Informations réseau locales** — Adresse IP, passerelle, interfaces.
- 🛣️ **Gestion des routes** — Affiche et modifie les routes système.
- 🧠 **Capture de paquets (Tshark)** *(optionnel)* — Analyse basique du trafic réseau.

---

## 🧩 Technologies utilisées

| Composant | Technologie |
|------------|-------------|
| Langage principal | Python 3 |
| Interface graphique | PyQt6 |
| SSH | Paramiko |
| Scans & diagnostic | Nmap, Tshark |
| Threads | QThread (PyQt) |
| OS cible | Linux (Ubuntu recommandé) |

---

## 🏗️ Installation

### 1️⃣ Cloner le projet
```bash
git clone https://github.com/<nrsRZK>/netassist.git
cd netassist

###2️⃣ Créer et activer un environnement virtuel
python3 -m venv venv
source venv/bin/activate

3️⃣ Installer les dépendances Python
pip install -r requirements.txt
    ⚙️ Si requirements.txt n’existe pas encore, tu peux le créer avec :
pip freeze > requirements.txt

4️⃣ Installer les outils système requis
sudo apt install nmap traceroute tshark

🖥️ Utilisation
source venv/bin/activate
python main.py

🧱 Structure du projet
network_assistant/
├─ main.py
├─ ui/
│  ├─ ping_tab.py
│  ├─ traceroute_tab.py
│  ├─ ssh_tab.py
│  ├─ nmap_tab.py
│  ├─ route_tab.py
│  ├─ ip_info_tab.py
│  └─ network_info_tab.py
├─ threads/
│  ├─ ping_thread.py
│  ├─ ssh_thread.py
│  ├─ scan_thread.py
│  ├─ route_thread.py
│  └─ traceroute_thread.py
├─ utils/
│  └─ helpers.py
├─ requirements.txt
└─ README.md

🧑‍💻 Auteur

👤 Roberto Razakandrandria
Étudiant en informatique, passionné par les réseaux, Linux et la cybersécurité.
📫 Mon profil GitHub
