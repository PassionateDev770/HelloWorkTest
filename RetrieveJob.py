import requests
import sqlite3
import json
from tkinter import *
from tkinter import ttk

'''
Après de multiples tentatives de connexion avec la clé fournie l'accès à l'API a été rejeté. J'ai utiliser l'API de Github pour les différentes tâches qui m'étaient demandées.
req = requests.get('http://api.emploi-store.fr:80/partenaire/offresdemploi?api_key=PAR_jobfetcher_394e0607bc151d4f9b2c394db02092bd105ecae8788b0565205866c7d5a99523')
res = req.json()
print(res)'''


#function which creates database to store data
def createDatabase():
    conn = sqlite3.connect('job.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS jobs (id integer primary key autoincrement, intitule TEXT, description integer, lieuTravail TEXT, typeContrat TEXT, entreprise TEXT)")
    conn.commit()
    conn.close()
    print("database created")
createDatabase()

#function which stores data retrieved from github API
def savedata():
    req = requests.get('https://api.github.com/users')
    print(req.status_code)

    data = json.loads(req.text)
    print(data)

    conn = sqlite3.connect('job.db')
    c = conn.cursor()
    for s in data:
        c.execute("INSERT INTO jobs (intitule, description, lieuTravail, typeContrat, entreprise) VALUES (?,?,?,?,?)", (s['type'], s['login'], s['node_id'], s['avatar_url'], s['url']))
        conn.commit()
    conn.close()
    print('Data stored')
savedata()

#Show the stored data in job sqlite db

def getDataFromDatabase():
    '''
    J'ai voulu utiliser Tkinter pour afficher les données mais le temps ne me le permettait pas
    window = Tk()
    window.title('Job list')
    window.geometry('800x800')
    window.resizable(False, False)
    window.mainloop() '''

    conn = sqlite3.connect('job.db')
    c = conn.cursor()
    data = c.execute("SELECT * FROM jobs")
    data = data.fetchall()
    #print("data", data)
    for i in data:
        print("Emploi: ", i[0])
        print("Intitulé: ", i[1])
        print("Description: ", i[2])
        print("Lieu de travail: ", i[3])
        print("Type de contrat: ", i[4])
        print("Entreprise: ", i[5])
        print("==========\n")




    conn.commit()
    conn.close()


getDataFromDatabase()