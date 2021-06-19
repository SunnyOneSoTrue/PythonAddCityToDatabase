import requests
import json
import sqlite3

conn = sqlite3.connect("Chuck_Norris_Jokes")
c = conn.execute("""CREATE TABLE IF NOT EXISTS Jokes (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    category VARCHAR(50),
                    joke VARCHAR(500),
                    url VARCHAR(500),
                    iconUrl VARCHAR(500))""")

jsonFile = open("jsonJokes.txt", 'w')

jokeCategories = [
    "animal",
    "career",
    "celebrity",
    "dev",
    "explicit",
    "fashion",
    "food",
    "history",
    "money",
    "movie",
    "music",
    "political",
    "religion",
    "science",
    "sport",
    "travel"
]

print("joke categories are:")
for category in jokeCategories:
    print(category)

category = input("please enter Chuck norris joke category you want displayed: ")
category = category.lower()

r = requests.get(f'https://api.chucknorris.io/jokes/random?category={category}')
# print(r.status_code)
# print(r.headers)
# print(r.headers['Content-Type'])
# print(r.text)

txt = r.json()
res = json.dumps(txt, indent=4)

jsonFile.write(f"{category}: {res}")

print(res)
print(category)
print(f"lon:{txt['id']}")
print(txt["value"])
print(txt["url"])

list = []

tuple = (f"{category}",
         f"{txt['icon_url']}",
         f"{txt['url']}",
         f"lon:{txt['value']}")
for i in tuple:
    list.append(i)

conn.execute("INSERT INTO Jokes(category, iconUrl, url, joke) VALUES (?, ?, ?, ?)", tuple)
conn.commit()

print(tuple)
conn.close()
