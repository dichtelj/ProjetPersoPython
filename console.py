from datetime import datetime

from Database.Database import Database
from Models.Eclipse import Eclipse
from Models.Eruption import Eruption
from Models.Evenement import Evenement

if __name__ == "__main__":
    db = Database()
    isOn = True
    while(True):
        print("Mode console")
        print("1 : Créer")
        print("2 : Supprimer")
        print("3 : Modifier")
        print("4 : Quitter")
        action = int(input("Sélectionner l'option désirée"))
        if action == 1:
            print("Création d'un objet")
            print("1 : Evènement")
            print("2 : Eruption")
            print("3 : Eclipse")
            action = int(input("Choisir l'objet à créer"))
            if action == 1:
                libelle = input("Libelle : ")
                dateDeb = input("Date de début : ")
                dateFin = input("Date de fin : ")
                pays = input("Pays : ")
                departement = input("Département (si France) : ")
                evenement = Evenement(libelle,dateDeb,dateFin,pays,departement)
                db.create(evenement, Evenement)
            if action == 2:
                libelle = input("Libelle : ")
                duree = input("Duree : ")
                date = input("Date : ")
                intensite = input("Intensite : ")
                eruption = Eruption(libelle,duree,date,intensite)
                db.create(eruption, Eruption)
            if action == 3:
                libelle = input("Libelle : ")
                dateDeb = input("Date de début : ")
                dateFin = input("Date de fin : ")
                pays = input("Pays : ")
                departement = input("Département (si France) : ")
                type = input("Type de l'eclipse (solaire ou lunaire) : ")
                eclipse = Eclipse(libelle,dateDeb,dateFin,pays,departement,type)
                db.create(eclipse, Eclipse)

        if action == 2:
            print("Choisissez ce que vous voulez supprimer.")
            print("1 : Evenement")
            print("2 : Eruption")                
            print("3 : Eclipse")
            action = int(input("Entrez le numéro de votre choix : "))
            if action == 1:
                id = input("Identifiant de l'évènnement à supprimer :")
                evenement = db.retrieve(Evenement, Evenement.id, id)
                if evenement != None:
                    db.delete(evenement, Evenement)
            if action == 2 :
                id = input("Identifiant de l'éruption à supprimer :")
                eruption = db.retrieve(Eruption, Eruption.id, id)
                if eruption != None:
                    db.delete(eruption, Eruption)

            if action == 3:
                id = input("Identifiant de l'eclipse à supprimer :")
                eclipse = db.retrieve(Eclipse, Eclipse.id, id)
                if eclipse != None:
                    db.delete(eclipse, Eclipse)
        if action == 3:
            print("Choisissez ce que vous voulez supprimer.")
            print("1 : Evenement")
            print("2 : Eruption")                
            print("3 : Eclipse")
            action = int(input("Entrez le numéro de votre choix : "))
            if action == 1:
                id = input("Identifiant de l'évènnement à modifier :")
                evenement = db.retrieve(Evenement, Evenement.id, id)
                if evenement != None:
                    evenement.libelle = input("Libelle :") or evenement.libelle
                    evenement.dateDeb = input("Date de début :") or evenement.dateDeb
                    evenement.dateFin = input("Date de fin :") or evenement.dateFin
                    evenement.pays = input("Pays :") or evenement.pays
                    evenement.departement = input("Département (si France) :") or evenement.departement
                    db.update(evenement, Evenement)
            if action == 2 :
                id = input("Identifiant de l'éruption à modifier :")
                eruption = db.retrieve(Eruption, Eruption.id, id)
                if eruption != None:
                    eruption.libelle = input("Libelle :") or eruption.libelle
                    eruption.duree = input("Duree :") or eruption.duree
                    eruption.intensite = input("Intensite :") or eruption.intensite
                    eruption.date = input("Date :") or eruption.date
                    db.update(eruption, Eruption)

            if action == 3:
                id = input("Identifiant de l'eclipse à modifier :")
                eclipse = db.retrieve(Eclipse, Eclipse.id, id)
                if eclipse != None:
                    evenement.libelle = input("Libelle :") or evenement.libelle
                    evenement.dateDeb = input("Date de début :") or evenement.dateDeb
                    evenement.dateFin = input("Date de fin :") or evenement.dateFin
                    evenement.pays = input("Pays :") or evenement.pays
                    evenement.departement = input("Département (si France) :") or evenement.departement
                    db.update(evenement, Evenement)
                                    
        if action == 4:
            boucle = True
