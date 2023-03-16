# Python-test

Ce projet permet les choses suivantes 

Scirpt : Films.py
-> Permet de retourner aléatoirement une phrase contenu dans un tableau, dans le terminal
-> Permet de retourner un personnage d'un dictionnaire sous forme d'objet JSON, dans le terminal

Script : Computer_Info.py
-> Permet de savoir les informations suivantes sur l'ordinateur qui lance le script : OS, Ram, processeur, Nom du pc
-> Affiche le tout grâce à un template via Jinja

Pré requis :

-> Installer python sur sa machine (scripts testés sur la version 3.11.2)
-> Vérifier que les imports sont bien présents
-> Pour le deuxième scirpt, vous aurez besoin de faire les imports suivant :
	- pip install py-cpuinfo
	- pip install jinja2
	- pip install psutil

Une fois cela fait, avec un "py films.py" et py Computeur_Info.py", vous pouvez lancer les scripts.