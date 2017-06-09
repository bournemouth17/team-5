#!/usr/bin/env python3
import cgi
import json

#järgmised kaks rida kuvavad erroreid, kui neid pruugib olla
import cgitb
cgitb.enable() 

keys = ["start_time", "player1", "player2", "points1", "points2", "game_time"]
form = cgi.FieldStorage() #loeb scriptile antud parameetreid
line = {}
for key in keys: 
    line[key] = form.getvalue(key)

history = []
try: 
    f = open("history.json", "r")
    history = json.loads(f.read()) #loeb ajaloo sisse ja json parsib seda
    f.close()
except FileNotFoundError: 
    pass

history.insert(0, line)
f = open("history.json", "w")
f.write(json.dumps(history)) #teisendab pythoni listi json formaati ja kirjutab faili
f.close



print("Content-Type: text/plain")
print()
print("ok")
print(line)
