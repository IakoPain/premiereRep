#┍-------------------------------------------------------------┑
#|Pain                        NSI                           1G7|
#|Iako                        DS3                              |
#├-------------------------------------------------------------┤
#|                        Sujet 3                              |
#└-------------------------------------------------------------┘
'''
codeMorseLettres=['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
codeMorseChiffres =['-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']

texte=str(input("votre texte ?"))
texte=texte.upper()
def nouveauTexte(texte):
    nTexte=""
    for n in range(len(texte)):
        if ord(texte[n])==65:
            nTexte+=(codeMorseLettres[0]+"   ")
        if ord(texte[n])==66:
            nTexte+=(codeMorseLettres[1]+"   ")
        if ord(texte[n])==67:
            nTexte+=(codeMorseLettres[2]+"   ")
        if ord(texte[n])==68:
            nTexte+=(codeMorseLettres[3]+"   ")
        if ord(texte[n])==69:
            nTexte+=(codeMorseLettres[4]+"   ")
        if ord(texte[n])==70:
            nTexte+=(codeMorseLettres[5]+"   ")
        if ord(texte[n])==71:
            nTexte+=(codeMorseLettres[6]+"   ")
        if ord(texte[n])==72:
            nTexte+=(codeMorseLettres[7]+"   ")
        if ord(texte[n])==73:
            nTexte+=(codeMorseLettres[8]+"   ")
        if ord(texte[n])==74:
            nTexte+=(codeMorseLettres[9]+"   ")
        if ord(texte[n])==75:
            nTexte+=(codeMorseLettres[10]+"   ")
        if ord(texte[n])==76:
            nTexte+=(codeMorseLettres[11]+"   ")
        if ord(texte[n])==77:
            nTexte+=(codeMorseLettres[12]+"   ")
        if ord(texte[n])==78:
            nTexte+=(codeMorseLettres[13]+"   ")
        if ord(texte[n])==79:
            nTexte+=(codeMorseLettres[14]+"   ")
        if ord(texte[n])==80:
            nTexte+=(codeMorseLettres[15]+"   ")
        if ord(texte[n])==81:
            nTexte+=(codeMorseLettres[16]+"   ")
        if ord(texte[n])==82:
            nTexte+=(codeMorseLettres[17]+"   ")
        if ord(texte[n])==83:
            nTexte+=(codeMorseLettres[18]+"   ")
        if ord(texte[n])==84:
            nTexte+=(codeMorseLettres[19]+"   ")
        if ord(texte[n])==85:
            nTexte+=(codeMorseLettres[20]+"   ")
        if ord(texte[n])==86:
            nTexte+=(codeMorseLettres[21]+"   ")
        if ord(texte[n])==87:
            nTexte+=(codeMorseLettres[22]+"   ")
        if ord(texte[n])==88:
            nTexte+=(codeMorseLettres[23]+"   ")
        if ord(texte[n])==89:
            nTexte+=(codeMorseLettres[24]+"   ")
        if ord(texte[n])==90:
            nTexte+=(codeMorseLettres[25]+"   ")
        if ord(texte[n])==48:
            nTexte+=(codeMorseChiffres[0]+"   ")
        if ord(texte[n])==49:
            nTexte+=(codeMorseChiffres[1]+"   ")
        if ord(texte[n])==50:
            nTexte+=(codeMorseChiffres[2]+"   ")
        if ord(texte[n])==51:
            nTexte+=(codeMorseChiffres[3]+"   ")
        if ord(texte[n])==52:
            nTexte+=(codeMorseChiffres[4]+"   ")
        if ord(texte[n])==53:
            nTexte+=(codeMorseChiffres[5]+"   ")
        if ord(texte[n])==54:
            nTexte+=(codeMorseChiffres[6]+"   ")
        if ord(texte[n])==55:
            nTexte+=(codeMorseChiffres[7]+"   ")
        if ord(texte[n])==56:
            nTexte+=(codeMorseChiffres[8]+"   ")
        if ord(texte[n])==57:
            nTexte+=(codeMorseChiffres[9]+"   ")

    return nTexte
print(nouveauTexte(texte))
'''
#┍-------------------------------------------------------------┑
#|                      Exercice 4.3                           |
#└-------------------------------------------------------------┘
'''
def Double(chaine):
    chaineDouble=""
    for i in range(len(chaine)):
        chaineDouble=chaineDouble+chaine[i]+chaine[i]
    return chaineDouble
print(Double("Test"))
'''