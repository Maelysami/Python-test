import random
import json

# Partie n°1
class CitationAleatoire:
    #  Créer un nouvel objet de la classe CitationAleatoire avec une liste de citations stockée dans l'attribut self.citations
    def __init__(self, citations):
        self.citations = citations
        
    # Fait appel à la bibliothèque random de Python
    # Utilise la méthode choice pour choisir une phrase aléatoire parmi les phrases stockées dans l'attribut self.phrases de l'objet CitationAleatoire
    # Retourne la phrase choisie
    def generer_phrase(self):
        return random.choice(self.citations)
        
# Affiche une citation aléatoire à partir de la liste de citations données dans citations[]
if __name__ == "__main__":
    # Exemple d'utilisation
    citations = ["You're a wizard, Harry", "Expecto Patronum", "I solemnly swear that I am up to no good", "Always"]
    phrase_aleatoire = CitationAleatoire(citations)
    print(phrase_aleatoire.generer_phrase())



# Partie n°2
class Personnage:

    # Initialise les attributs pour le personnage
    def __init__(self, age, prenom, role):
        self.age = age
        self.prenom = prenom
        self.role = role

    # Retoune le dictionnaire du personnage sous la forme d'un objet JSON
    def to_json(self):
        return json.dumps({
            'age': self.age,
            'prenom': self.prenom,
            'role': self.role
        })

# Création d'un objet Personne avec les attributs spécifiés
personne = Personnage(15, 'Harry', 'Potter')

# Affichage du dictionnaire personnage sous forme d'objet JSON dans le terminal
print(personne.to_json())

