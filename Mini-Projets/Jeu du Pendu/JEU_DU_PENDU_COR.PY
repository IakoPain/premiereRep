
motadeviner="bonjour"   # mot à chercher
motachercher="*******"  # mot à deviner les étoiles seront remplacées au fur et à mesure
nblettres=0             # compteur du nombre de lettres saisies par l'utilisateur

def remplaceLettre(lettre,motadeviner,motachercher):
    nouveauMot=""
    for i in range(len(motadeviner)):
        if motadeviner[i]==lettre:
            nouveauMot+=lettre
        else:
            nouveauMot+=motachercher[i]
    return nouveauMot


while nblettres<10 and motachercher.count('*')!=0:
    lettre=input("votre lettre ")
    nblettres+=1
    motachercher=remplaceLettre(lettre,motadeviner,motachercher)
    print(motachercher)

if motachercher.count('*')==0:
    print("bravo en",nblettres,"coups")
else:
    print("perdu")








