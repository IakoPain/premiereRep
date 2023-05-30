#┍-------------------------------------------------------------┑
#|                           Exo 1                             |
#└-------------------------------------------------------------┘
"""
brailles = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢','⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅','⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵']

def affichagebaille(texte):
    texte=texte.upper()
    texteBraille=''
    for c in range(0,len(texte)):
        if texte[c]>=" " and texte[c]<"Z":
            texteBraille+=brailles[ord(texte[c])-32]
    return texteBraille
	#a completer
    return texteBraille


texte=str(input("votre texte ?"))
print(affichagebaille(texte))
"""
#┍-------------------------------------------------------------┑
#|                           Exo 2                             |
#└-------------------------------------------------------------┘
"""
def insertionTexte(texte):
    nouveauTexte=''
    for indice in range(len(texte)-1):
        nouveauTexte += texte[indice]+ "*"
    nouveauTexte+=texte[-1]
    return nouveauTexte

texte=str(input("Texte ?"))
print(insertionTexte(texte))
"""
#┍-------------------------------------------------------------┑
#|                           Exo 3                             |
#└-------------------------------------------------------------┘
"""
def inversionMot(texte):
    nouveauTexte=""
    for i in range(len(texte)-1,-1,-1):
        nouveauTexte+=texte[i]
    return nouveauTexte
texte=str(input("Texte ?"))
print(inversionMot(texte))
"""
#┍-------------------------------------------------------------┑
#|                           Exo 4                             |
#└-------------------------------------------------------------┘
"""
def palindrome(texte):
    for i in reversed(0,len(texte)):
        print(i)
    return
"""
#┍-------------------------------------------------------------┑
#|                           Exo 5                             |
#└-------------------------------------------------------------┘
def cesar(texte):
    texte.lower
    for i in range(0,len(texte)):

texte=str(input("Texte ?"))
shift=int(input("Shift ?"))





#97-122











