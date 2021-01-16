import os, sys, random, json

theliste = input("choisissez le fichier liste: ")
n_max = int(input(" Nombre de personnes max par groupe: "))


with open(theliste, "r", encoding="utf-8") as i:
    liste_noms = i.readlines()

# print(liste_noms)


n_guy = len(liste_noms)
if n_guy % n_max ==0:
    n_groupes = (n_guy//n_max)
else:
    n_groupes = (n_guy//n_max)+1


liste_groupes = {}      
x = 1
while x <= n_groupes:
    liste_groupes["Groupe n°"+str(x)]=[]
    x+=1
# print(liste_groupes)

i = 1
while i <= n_max:
    index = 1
    for le_groupe in liste_groupes:
        # print(le_groupe)
        try:
            if n_guy > 0:
                n_guy = len(liste_noms)
                # index_choice = random.choice(liste_noms)
                index_pioche = random.randrange(n_guy)
                nom_pioche = liste_noms[index_pioche]
                liste_groupes["Groupe n°"+str(index)].append(nom_pioche.strip("\n"))
                liste_noms.remove(nom_pioche)
                index += 1
                with open("Liste_des_groupes.json", "a") as f :
                    json.dump(liste_groupes, f)
            
        except:
            break
    i += 1
print(liste_groupes)
                

