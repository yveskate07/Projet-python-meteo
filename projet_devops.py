import requests # pour lancer les requêtes HTTP
import pprint # pour formater la reponse obtenue en format json
print ("Bienvenu(e) sur l'application qui vous offre les informations meteorologique du monde entier")
API_Key = '0f70f1694a9a05acfae04d35479d6b49' # clé API récupérée sur le site openweathermap.org
city = input("veuillez saisir votre ville: ") # le nom de la ville dont on souhaiterais obtenir les informations météorologiques
base_url =f"https://api.openweathermap.org/data/2.5/weather?appid={API_Key}&q={city}" # l'url vers la page qui contient les informations recherchées
weather_data=requests.get(base_url).json() # lancement de la requête HTTP vers l'url ci-dessus
print(weather_data) # affichage de la reponse obtenue sous format JSON
