import hashlib

mdp = input("saisir votre mot de passe : ")


def verif_mdp(mdp):
    list_lettres = []
    list_chi_carspé = []
    nbr_maj, nbr_min, nbr_carspé, nbr_chiffre = 0, 0, 0, 0

    if len(mdp) < 8:
        return "le mot de passe doit contenir au minimum 8 caractères"

    for i in mdp:
        if 65 <= ord(i) <= 90: #compris entre A et Z 
            list_lettres.append(i)
        elif 97 <= ord(i) <= 122: #compris entre a et z 
            list_lettres.append(i)
        else:
            list_chi_carspé.append(i)

    if len(list_lettres) == 0:
        return "Le mot de passe doit contenir au moins une lettre"

    for Mot in list_lettres:
        if Mot.isupper(): # si Mot est majuscule
            nbr_maj += 1 # on ajoute 1
            if nbr_maj == len(list_lettres): # si toutes les lettres sont des majuscules
                return "Votre mot de passe doit contenir au moins une minuscule"
        if Mot.islower(): # si Mot est minuscule
            nbr_min += 1 # on ajoute 1
            if nbr_min == len(list_lettres): #si toutes les lettres sont des minuscules
                return "Votre mot de passe doit contenir au moins une majuscule"

    if len(list_chi_carspé) == 0:
        return "Votre mot de passe doit contenir au moins un chiffre"

    for k in list_chi_carspé:
        if k not in ['!', '@', '#', '$', '%', '^', '&', '*']:
            nbr_carspé += 1
            if nbr_carspé == len(list_chi_carspé):
                return "Votre mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *)"
        if k not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            nbr_chiffre += 1
            if nbr_chiffre == len(list_chi_carspé):
                return "Votre mot de passe doit contenir au moins un chiffre"


result = verif_mdp(mdp)

if result == None:
    print('Mot de pass correct')
else:
    while result != None:
        print(result)
        nouveau_mdp = input("Tapez votre mot de passe : ")
        result = verif_mdp(nouveau_mdp)

    hashlib.sha256(nouveau_mdp.encode()).hexdigest()
    print('Mot de passe correct')