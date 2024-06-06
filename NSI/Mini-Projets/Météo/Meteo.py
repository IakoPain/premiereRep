import requests, json

# votre clé API ici
api_key = "3e19222d52d5e0f07061377a10fab89b"

# URL de base
base_url = "http://api.openweathermap.org/data/2.5/weather?"

proxies = {
 "http": "http:172.30.137.29:3128",
 "https": "http:172.30.137.29:3128",
}


def recupereMeteo(ville):
    # url de la requete
    url = base_url + "appid=" + api_key + "&q=" + ville
    print("l'url est",url)
    print("--------------------------------------------------")
    # methode get de la requete sur le site openweathermap
    response = requests.get(url,proxies=proxies)
    # response qui va être convertit en dictionnaire
    dict = response.json()
    print("données completes",dict)
    print()
    print(dict.keys())
    print("--------------------------------------------------")
    # récupère la clé main
    main = dict["main"]
    print("données de la clé main",main)
    print("--------------------------------------------------")
    #A compléter
    pression=main['pressure']
    temperature=main['temp']-273.15
    humidite=main['humidity']
    return (pression,temperature,humidite)

class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('meteo.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        self.comboBox_Ville.addItems(["Le Mans", "Lille", "Bayonne"])
        #Quand on clique sur le pushButton, on appelle la méthode boutonOK
        self.pushButton_Maj.clicked.connect(self.boutonMaj)
        #Quand on clique sur le pushButtonAPropos, on appelle la méthode APropos
        self.pushButton_APropos.clicked.connect(self.APropos)
        self.show()             #affiche la fenêtre MainWindows

    def boutonMaj(self):
        print('bouton cliqué')
        #A compléter
        #self.label_Temperature.setText('{0:.2f}°C'.format(meteo[1]))


    def APropos(self):      #Gestion du message A Propos
        msg = QMessageBox()
        #A compléter

    def paintEvent(self, event):    #Evènement paint pour afficher l'image de fond
        painter = QPainter(self)
        #A compléter (charger l’image de fond)

meteo=recupereMeteo("Le Mans")  #exécute la fonction gérant la requête GET
print("affichage du tuple", meteo) # affiche les 3 valeurs sous forme de tuple
print("pression",meteo[0]) # affiche la pression
print("temperature",meteo[1]) # affiche la température
print("humidite",meteo[2]) # affiche l'humidité