import requests
import os

api_key = '071c611aadaf047c433ba7e25800ac1d'
os.system('cls')

user_input = input("Inserta la ciudad:")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&appid={api_key}")

if weather_data.json()['cod'] == '404':
    print("No se encuentra esta ciudad.")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])  

    print(f"El clima en {user_input} es: {weather}") #no supe como ponerlo en español F :C
    print(f"La temperatura en {user_input} es de: {temp}ºC")
    input ("presiona cualquier tecla para salir!!!")