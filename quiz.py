import requests
import json
import sqlite3

conn = sqlite3.connect("Cities")
c=conn.execute("""CREATE TABLE IF NOT EXISTS CityInfo (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    City VARCHAR(50),
                    weather VARCHAR(10),
                    timezone VARCHAR(100),
                    coordinates VARCHAR(100))""")

jsonFile = open("jsonInfo.txt",'w')

key='3373b08e49b718d1b3073d16d01da1e8'
city = input("please enter city:")

r = requests.get( f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric')
# print(r.status_code)
# print(r.headers)
# print(r.headers['Content-Type'])
# print(r.text)

txt = r.json()
res = json.dumps(txt, indent=4)

jsonFile.write(f"{city}: {res}")

# print(res)
# print(city)
# print(f"lon:{txt['coord']['lon']}, lat{txt['coord']['lat']}")
# print(txt["weather"][0]["main"])
# print(txt["timezone"])
list = []

tuple = (f"{city}",
        f"{txt['weather'][0]['main']}",
        f"{txt['timezone']}",
        f"lon:{txt['coord']['lon']}, lat{txt['coord']['lat']}")
for i in tuple:
    list.append(i)

conn.execute("INSERT INTO CityInfo(City, weather, timezone, coordinates) VALUES (?, ?, ?, ?)", tuple)
conn.commit()

print(tuple)
conn.close()