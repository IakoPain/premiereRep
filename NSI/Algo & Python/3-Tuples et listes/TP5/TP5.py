#┍-------------------------------------------------------------┑
#|                          Exemple                            |
#└-------------------------------------------------------------┘
"""
from PIL import Image,ImageDraw,ImageFont
img=Image.new('RGB',(256,256),(0,0,0))



largeur,hauteur=img.size
draw=ImageDraw.Draw(img)
draw.line((0,0,largeur,hauteur),fill=(0,255,0))

draw.line((10,20,100,200),fill=(255,0,0))
img.show()
"""
#┍-------------------------------------------------------------┑
#|                          Exo 1                              |
#└-------------------------------------------------------------┘
"""
from PIL import Image,ImageDraw,ImageFont
img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def traceDroite(nbDroites,ecart):
    for j in range(1,nbDroites):
        draw.line((0+ecart,0,0+ecart,256),(0,255,0))
        ecart=ecart+20
traceDroite(10,20)

img.show()
"""
#┍-------------------------------------------------------------┑
#|                          Exo 2                              |
#└-------------------------------------------------------------┘
"""
from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def cercle(x,y,rayon,couleur):
    draw.ellipse((x-rayon,y-rayon,x+rayon, y+rayon),fill=couleur)

def tracecible():
    draw.ellipse((68,68,188,188),(0,0,255))
    draw.ellipse((88,88,168,168),(255,0,0))
    draw.ellipse((108,108,148,148),(255,255,0))

tracecible()
img.show()
"""
#┍-------------------------------------------------------------┑
#|                          Exo 3                              |
#└-------------------------------------------------------------┘
"""
from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(255,255,255))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def rectangle(x,y,largeur,hauteur,couleur):
    draw.rectangle((x,y,x+largeur, y+hauteur),fill=couleur)

def traceEffetVisuel():
    c=0
    d=0
    for n in range(1,256,10):
        for u in range(1,256,10):
            rectangle(u,n,5,5,(0,0,0))



traceEffetVisuel()
img.show()
img.save("effet.png")
"""
#┍-------------------------------------------------------------┑
#|                         Exo 4.1                             |
#└-------------------------------------------------------------┘
"""
from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
for y in range(hauteur):
    for x in range(largeur):
         img.putpixel((x,y),(255-y,0,0))
img.show()
img.save("degrade_rouge.jpg")
"""
#┍-------------------------------------------------------------┑
#|                         Exo 4.2                             |
#└-------------------------------------------------------------┘
"""
from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
for x in range(hauteur):
    for y in range(largeur):
         img.putpixel((x,y),(0,0+x,0))
img.show()
img.save("degrade_vert.jpg")
"""
#┍-------------------------------------------------------------┑
#|                           Exo 5                             |
#└-------------------------------------------------------------┘
"""
from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
for y in range(hauteur):
    for x in range(largeur):
         img.putpixel((x,y),(255-x,0+y,255-x))
img.show()
img.save("degrade_bicolor.jpg")
"""
#┍-------------------------------------------------------------┑
#|                          Exo 6                              |
#└-------------------------------------------------------------┘
"""
from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(1536,256),(0,0,0))
largeur,hauteur=img.size
for y in range(hauteur):
    for x in range(0,256):
        img.putpixel((x,y),(255,0+x,0))
    for x in range(256,512):
        img.putpixel((x,y),(512-x,255,0))
    for x in range(512,768):
        img.putpixel((x,y),(0,255,-512+x))
    for x in range(768,1024):
        img.putpixel((x,y),(0,1024-x,255))
    for x in range(1024,1280):
        img.putpixel((x,y),(-1024+x,0,255))
    for x in range(1280,1536):
        img.putpixel((x,y),(255,0,1536-x))
img.show()
img.save("degradex6.jpg")
"""
#┍-------------------------------------------------------------┑
#|                          Exo 7                              |
#└-------------------------------------------------------------┘

from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size

title=[]
for n in range(0,12):
    print('{:02d}.png'.format(n))
    title.append(Image.open('{:02d}.png'.format(n)))


map=[[1,5,5,5,10,5,5,2],
     [6,0,0,0,6,0,0,6],
     [6,0,0,0,6,0,0,6],
     [6,0,0,0,6,0,0,6],
     [6,0,0,0,6,0,0,6],
     [6,0,0,0,6,0,0,6],
     [6,0,0,0,6,0,0,6],
     [3,5,5,5,8,5,5,4]]

for ligne in range(0,8):
    for colonne in range(0,8):
        numero=map[ligne][colonne]
        print(map[ligne][colonne],end=' ')
        img.paste(title[numero], (colonne*32,ligne*32))
    print()


img.show()
img.save("map.png")
