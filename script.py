import os, sys, random

theliste = input("choisissez le fichier liste: ")
n_max = input(" Nombre de personnes max par groupe: ")

def open_thefile():
    with open(theliste, "r", encoding="utf-8") as i:
        liste_noms = i.readlines()
        return liste_noms
    
def Nombre_groupes():
    
    for i in liste_noms:
        if len(list_noms)%(n_max)==0:
            n_groupes = len(liste_noms)//(n_max)
        else:
            n_groupes = len(liste_noms)//(n_max)+1
return n_groupes

def groupes_vide():
    liste_groupe = {}
    x = 1
    while i <= n_groupes:
        groupes_vide["Groupe n°"+str(x)]=[]
        x+=1
        return groupes_vide

def personnes_groupe():
    
    for a in liste_noms:
        nom_groupe = i.append(liste_groupe)
        for a in liste_groupe:
            if count(a)>1:


def j_son():




            

# def f_groupe(len(count), nbrmax):


# donnees = {"clé" : "valeur"}
# with open("chemin/du/fichier.json", "w") as compo:
#     json.dump(donnees, compo)

