#Lien GitHub du projet app_pointage: https://github.com/binetouguey3s/gestion_presence

#Application de pointage

#Liste de stockage des apprenants
apprenants = [] #apprenants pas au singulier

#Dictio de suivi des presences
presences = {}

#Debut ajouter un apprenant 
def ajout_apprenant():
    print("-"*10,"1.Ajouter les infos de l'apprenant","-"*10)

    try:
        #Gerons et saisissons le nom
        while True:
            nom = input("Nom: ").strip().lower()
            if nom.isalpha():
                break
            else:
                print("Mettez uniquement des lettres svp")  

        #Gerons et saisissons le prenom
        while True:
            prenom = input("Prénom: ").strip().lower()
            if nom.isalpha():
                break
            else:
                print("Mettez uniquement des lettres svp")  

        #Gerons et saisissons la promo
        while True:
            promo = input("Promo (ex: p4): ").strip().lower()
            if promo.startswith("p") and promo[1:].isdigit():
                break
            else:
                print("Mettez uniquement ce genre de format: p4 par exemple")

        #Gerons et saisissons l'identifiant
        while True:
            identifiant = input("Identifiant unique: ").strip().lower()
            if identifiant == " ":
                print("L'identifiant ne peut pas être vide.")
            else:
                break

        #Si l'P1apprenant eXiste deja
        for etudiant in apprenants:
            if etudiant["identifiant"] == identifiant:
                print(f"Erreur: L'identifiant '{identifiant}' existe déjà.")
                return()
            

        #  condition pour la promo 
            if len(promo) == 2 and promo[0] =='p' and promo[1].isdigit():
                break
            else:
                print("Format de promo invalide. Utilisez le format 'pX' où X est un chiffre.")
                return()
         # Fin de if len(promo)     
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
        apprenants.append(nouveau_apprenant)

        print(f"_"*5,"Apprenant ajouté","_"*5)
    except:
        print("Donner de bon identifiant")
# Fin ajouter un apprenant 


#Debut enregistrer la presence pour la seance du jour, en marquaunt chaque apprenant comme: present ou absent

def enregistre_presence():

    if len(apprenants) == 0:
        print("Pas d'apprenant dans cete liste")
        return()
    print("-"*10,"2.Enregistrement des présences","-"*10)
    print("Pour chaque apprenant, entrer soit 1 pour marquer sa presence ou bien 0 si il est absent:")
 
    for etudiant in apprenants:
        identifiant = etudiant["identifiant"]
        print(f" \n. {etudiant['prenom']} {etudiant['nom']} de la promo {etudiant['promo']} \n")
        
        while True:
            try:
                choix = input("\n Choisir entre: \n 1 = present \n 0 = absent \n===> ")

                if choix == "1":
                    presence = True  #  True = present
                    presences[identifiant] = presence
                    print(f"L'apprenant {etudiant['prenom']}  {etudiant['nom']} est present")
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
    if len(apprenants) == 0:
        print("Pas d'apprenant dans cete liste")
        return()
    print("-"*10,"\n3.Les apprenants presents sont:\n","-"*10)
    
    presence = False 
    for etudiant in apprenants:
        identifiant = etudiant["identifiant"]
        presence = presences.get(identifiant)

        if presence is True:
            print(f"\n{etudiant['prenom']} {etudiant['nom']} de la {etudiant['promo']} avec comme identité: {identifiant}\n") 
            presence =  True
        else:
            print("Pas de presence ")
#Fin affichage des apprenants presents

#Fonction de calcul du taux de presence
def taux_presence():

   #initier test 

   #fin initier test

    if len(apprenants) == 0:
        print("-"*2,"Pas d'apprenant dans cete liste","-"*2)
        return()
    
    total = len(apprenants) #Nombre total d'apprenants dans la liste
    venue = 0


    for etudiant in apprenants:
        identifiant = etudiant["identifiant"]
        presence = presences.get(identifiant)

        if presence is True: 
            venue = venue + 1

    taux = 0  #initialisation du taux
    if total > 0:
        taux = (venue / total) * 100

    #Debut test de choix
    print("-"*10,"Affichage des taux de presences par apprenants","-"*10)
    print("\na: Nombre total d'apprenants\n")
    print("\nb: Nombre d' apprenant présents\n")
    print("\nc: Nombre d' apprenant absents\n")
    print("\nd: Taux de présence\n")
    print("\ne: Retourner sur le MENU PRINCIPAL\n")

    while True:
        
        choix = input("Choisir entre  a et e:").lower().strip()
        if choix == "a":
            print(f"\n------Nombre total d'apprenants: {total}\n")
        elif choix == "b":
            print(f"\n------Nombre d' apprenant présents: {venue}\n")
        elif choix == "c":
            print(f"\n------Nombre d' apprenant absents: {total - venue}\n")
        elif choix == "d":
            print(f"\n------Taux de présence: {taux}% \n")
        elif choix == "e":
            print("------Retour sur le menu principal")
            break  
        else:
            print("------choisir entre a et e") 
        #fin de test
 


 #affiche tout
    #     print("\nInformations sur les presences enregistrées\n")
    #     print(f"\nNombre total d'apprenants: {total}\n")
    #     print(f"\nNombre d' apprenant présents: {venue}\n")
    #     print(f"\nNombre d' apprenant absents: {total - venue}\n")
    #     print(f"\nTaux de présence: {taux}%\n")
    # else:
    #     print("Pas de presence qui nous permet de calculer le taux de presence")        
#fin affiche tout 

# liste de tous les apprenants
def afficher_tous_apprenants():
    if len(apprenants) == 0:
        print("\n Aucun apprenant pour l'instant")
        return()
    
    print("\n--- Liste de tous les apprenants ---")
    for i, etudiant in enumerate(apprenants, 1):
        identifiant = etudiant["identifiant"]
        presence = presences.get(identifiant)
        
        if presence is True:
            statut = "présent"
        elif presence is False:
            statut = "absent"
        else:
            statut = "pas dans la liste"
        print(f"{i} ==> {etudiant['prenom']} {etudiant['nom']} de la {etudiant['promo']} avec comme id: {identifiant} est  {statut}")

#Fonction principale
def main():
    print("-"*20,"\nApplication de pointage\n","-"*20)
    print("-"*8,"\nMENU PRINCIPAL\n","-"*8)
    print("\n1: Ajouter un apprenant\n")
    print("\n2: Enregistrer la presence pour la seance du jour\n")
    print("\n3: Affichage des apprenants presents\n")
    print("\n4: Calcul du taux de presence\n")
    print("\n5: Afficher_tous_apprenants()\n")
    print("\n6: Quitter le programme\n")

    while True:
        
        choix = input("\n Choisir entre 1 et 6: " " ")

        if choix == "1":
            ajout_apprenant()
        elif choix == "2":
            enregistre_presence()
        elif choix == "3":
            affiche_presence()
        elif choix == "4":
            taux_presence()
        elif choix == "5":
            afficher_tous_apprenants()
        elif choix == "6":
            print("Quitter le programme")
            break
        else:
            print("Veuillez entrer svp un nombre entre 1 et 6")
main()  

#remarque du coach , mettre tous les apprenants dans une liste et apres afficher  la possibilite de choisir entre les apprenants selon leur id et pouvoir si possible les modifier , c' est a dire acceder aux infos et les changer
# inferieur : <
# superieur : >
