import requests
import pyfiglet
import os
from colorama import Fore
class pattern:
    def weather_app(self,autoreset=True):
        b=pyfiglet.figlet_format('Weather App')
        print(Fore.GREEN+b)
class weather:
    def __init__(self,_city,autoreset=True):
        self._city=_city
    def display(self):
        return self._city
try:
    c=pattern()
    c.weather_app()
    n=input("enter the name of the city which you want to know the temperature")
    a=weather(n)
    x=a.display()
    b=requests.get(f"http://api.weatherapi.com/v1/current.json?key=d2acf64e8b6e4288b58122130250712&q={x}&aqi=no")
    os.system('cls')
    c.weather_app()
    y=b.json()
    with open('data.json','w') as fs:
        fs.write(f"{b.json()}")
    print(f"name of the city:-{y['location']['name']}")
    print(f"Temperature in Celcius:- {y['current']['temp_c']}")
    print(f"Temperature in Fahrenheit:- {y['current']['temp_f']}")
    print(f"Humidity:-{y['current']['humidity']}")   
except requests.exceptions.ConnectionError as e:
    print("no internet connection are available please connect to the internet after run this code ")
except Exception as e:
    print(e)
        
    



