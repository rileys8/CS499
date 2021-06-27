from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint
from datetime import datetime

# MongoDB database
client = MongoClient('mongodb://localhost:27017')
database = client["AAC"]
collection = database["animals"]

def age(p):
    ageInDays = []
    for p in p:
        DOB = p['Date of Birth']
        outcomeDate = p['MonthYear']

        then = datetime.strptime(DOB, '%m/%d/%Y')
        now = datetime.strptime(outcomeDate, '%m/%d/%Y %H:%M:%S %p')

        elapsed = now - then
        days = elapsed.days
        ageInDays.append(days)

    average_age = 0
    for ele in range(0, len(ageInDays)):
        average_age = average_age + ageInDays[ele]
    average_age = round(average_age / len(ageInDays))
    return average_age

adoptedDogs = []
i = collection.find({"Animal Type": "Dog", "Outcome Type": "Adoption"},
                    {"_id": False, "Animal ID": False, "Name": False, "DateTime": False, "Outcome Type": False,
                     "Animal Type": False, "Sex upon Outcome": False, "Age upon Outcome": False, "Breed": False,
                     "Color": False, "Outcome Subtype": False})
for animals in i:
    adoptedDogs.append(animals)
days = (age(adoptedDogs))
years = round(days / 365, 1)
print("The average age of an adopted dog is " + str(years) + " years old or " + str(days) + " days old.")



adoptedCats = []
i = collection.find({"Animal Type": "Cat", "Outcome Type": "Adoption"},
                    {"_id": False, "Animal ID": False, "Name": False, "DateTime": False, "Outcome Type": False,
                     "Animal Type": False, "Sex upon Outcome": False, "Age upon Outcome": False, "Breed": False,
                     "Color": False, "Outcome Subtype": False})
for animals in i:
    adoptedCats.append(animals)
days = (age(adoptedCats))
years = round(days / 365, 1)
print("The average age of an adopted cat is " + str(years) + " years old or " + str(days) + " days old.")
