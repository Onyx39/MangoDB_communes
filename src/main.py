from pymongo import MongoClient
import pprint
import time

client = MongoClient('localhost', 27017)
db = client.France
collection = db.communes

print(db.list_collection_names())

# for post in collection.find({"code_departement": 39}):
#     pprint.pprint(post)

def calcul_temps (nom) :
    start = time.time()
    res = collection.find({"nom_commune" : nom})
    print(str(res))


    end = time.time()
    temps = round(1000000*(end - start))
    print(end - start)
    return "Le temps d'execution est de " + str(temps) + "µs."

print(calcul_temps("Annecy"))

