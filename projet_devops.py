import requests
import pprint
print ("Bienvenu sur l'application le site qui vous offre les  informations meteologique du monde entier")
API_Key = '0f70f1694a9a05acfae04d35479d6b49'
city = input("veiilez saisir votre ville: ")
base_url =f"https://api.openweathermap.org/data/2.5/weather?appid={API_Key}&q={city}"
weather_data=requests.get(base_url).json()
print(weather_data)

