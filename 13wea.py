import requests
from datetime import datetime
from pprint import pprint

now = datetime.now()

def city():
    
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Kiev&appid=81b241c58e62b70d2651a38bb3fa2169&units=metric$mode=html")
    weather = response.json()
    global weather

    print("Name your city: ")
    pprint(weather['name'])

def geo():
    
    print("1. Geo Location: ")
    pprint(weather['coord'])

def temp():
    print("2. Temperature: a) min, b) max")
    pprint(weather['main']['temp_min'])
    pprint(weather['main']['temp_max'])

def pressure():
    print("3. Pressure: ")
    pprint(weather['pressure']['unit'])

def f_weather():
    print("Full weather forecast ==>")
    
    print("1. Date now")
    print(now)
    
    print("2. Temperature: a) min, b) max")
    pprint(weather['main']['temp_min'])
    pprint(weather['main']['temp_max'])
    
    print("3. Wind")
    pprint(weather['wind'])
    
    print("4. Clouds")
    pprint(weather['clouds'])
    
    print("5. Pressure")
    #pprint(weather['pressure']) не могу получить ответ с сайта
    
    print("6. Describing the weather")
    pprint(weather['weather'])
    
class sqlLitePython():
    def Datebase():
        con = sqlite3.connect(":memory:")
        cur = con.cursor()
        cur.executescript("""
            create table Weather(
                  date,
                  temperature,
                  wind,
                  clouds,
                  pressure,
                  describing the weather
             );
             insert into Weather(date, temperature, wind, clouds, pressure, describing the weather)
             values (
                  'print(now)',
                  'pprint(weather['main']['temp_min'])
                   pprint(weather['main']['temp_max'])',
                  'pprint(weather['wind'])',
                  'pprint(weather['clouds'])',
                  '',
                  'pprint(weather['weather'])'
          
             );
             """)
    


if __name__ == '__main__':

    city()
    geo()
    temp()
#    pressure()
    f_weather()











    
