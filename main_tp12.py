#Lien GitHub du projet app_pointage: 

#Application de pointage

#Liste de stockage des apprenants
apprenant = []

#Dictio de suivi des presences
presences = {}

#Debut ajouter un apprenant 
def ajout_apprenant():
    try:
        print("Ajouter les infos de l'apprenant ")
        nom = input("Nom: ").strip()
        prenom = input("Prénom: ").strip()
        promo = input("Promo (ex: p4): ").strip()
        identifiant = input("Identifiant unique: ").strip()


        #Cas ou l' apprenant est deja identifié
        for etudiant in apprenant:
            if etudiant["identifiant"] == identifiant:
                print(f"Erreur: L'identifiant '{identifiant}' existe déjà.")
                return()
            
        #Ajout de l'apprenant dans un disctionnaire

        nouveau_apprenant = {
            "nom": nom,
            "prenom": prenom,
            "promo": promo,
            "identifiant": identifiant
        }

        #initialisons les presences
        presences[identifiant] = None

        #Ajout de liste des infos perso sur l'apprenant
        apprenant.append(nouveau_apprenant)

        print(f"Apprenant ajouté ")
    except ValueError:
        print("Donner de bon identifiant")
# Fin ajouter un apprenant 


#Debut enregistrer la presence pour la seance du jour, en marquaunt chaque apprenant comme: present ou absent

def enregistre_presence():
    if len(apprenant) == 0:
        print("Pas d'apprenant dans cete liste")
        return()
    print("\n Enregistrement des présences")
    print("Pour chaque apprenant, entrer soit 1 pour sa presence ou bien 0 si il est absent:")
 
    for etudiant in apprenant:
        identifiant = etudiant["identifiant"]
        print(f" \n {etudiant['prenom']} {etudiant['nom']} -Promo: {etudiant['promo']}")
        
        while True:
            try:
                choix = input("Choisir \n 1 = present et 0 = absent ").strip()

                if choix == "1":
                    presence = True  #  True = present
                    presences[identifiant] = presence
                    print(f" {etudiant['prenom']}  {etudiant['nom']} est present")
                    break
                elif choix == "0":
                    presence = False  # False = absent
                    presences[identifiant] = presence
                    print(f" {etudiant['prenom']} {etudiant['nom']} est  absent")
                    break
                else:
                    print("Saisir 0 ou 1 uniquement!")
            except:
                print("Erreur de saisie")
#fin Enregistrer la presence pour la seance du jour


#Affichons les apprenants presents
#Apres avoir obtenu la liste de tous les apprenants

#Fonction d'affichage des apprenants presents
def affiche_presence():
    if len(apprenant) == 0:
        print("Pas d'apprenant dans cete liste")
        return()
    print("Les apprenants presents:")

    etudiant_present = False
    for etudiant in apprenant:
        identifiant = etudiant["identifiant"]
        presence = presences.get(identifiant)

        if presence is True:
            print(f" {etudiant['prenom']} {etudiant['nom']} de la {etudiant['promo']} avec comme identité {identifiant}") 
            etudiant_present =  True
        else:
            print("Pas de presence ")
#Fin affichage des apprenants presents

#Fonction de calcul du taux de presence
def taux_presence():
    if len(apprenant) == 0:
        print("Pas d'apprenant dans cete liste")
        return()
    total = len(apprenant)
    venue = 0

    for etudiant in apprenant:
        identifiant = etudiant["identifiant"]
        presence = presences.get(identifiant)

        if presence is True: 
            venue = venue + 1

    if total > 0:
        taux = (venue / total) * 100
        print("Informations sur les presences enregistrées\n")
        print(f"Nombre total d'apprenants: {total}")
        print(f"Nombre d' apprenant présents: {venue}")
        print(f"Nombre d' apprenant absents: {total - venue}")
        print(f"Taux de présence: {taux}%")
    else:
        print("Pas de presence qui nous permet de calculer le taux de presence")        


#Fonction principale
def main():
    print("Application de pointage")
   
    while True:
        ajout_apprenant()
        enregistre_presence()
        affiche_presence()
        taux_presence()
main()   
