import platform
import cpuinfo
import socket
import os
from jinja2 import Environment, FileSystemLoader
import psutil


class Systeme:
    # Initialise les attributs de la classe Systeme
    def __init__(self):
        self.os = platform.system() + " " + platform.release()

        cpu_info = cpuinfo.get_cpu_info()
        if 'brand' in cpu_info:
            self.processor = cpu_info['brand']
        else:
            self.processor = 'Unknown'

        self.ram = str(round(psutil.virtual_memory().total / (1024.0 ** 3), 2)) + " GB"
        self.hostname = socket.gethostname()

# Crée une instance de la classe Systeme pour récupérer les informations système
systeme = Systeme()

# Charge le template HTML avec Jinja
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Génère le HTML avec les informations système
output = template.render(os=systeme.os, processor=systeme.processor, ram=systeme.ram, hostname=systeme.hostname)

# Écrit le HTML généré dans un fichier index.html
with open('index.html', 'w') as file:
    file.write(output)
