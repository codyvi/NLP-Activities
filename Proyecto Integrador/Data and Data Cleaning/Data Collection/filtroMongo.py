import pymongo
import credentials
import csv

myclient = pymongo.MongoClient("mongodb+srv://" + credentials.MONGO_USER + ":" + credentials.MONGO_PASSWORD + "@cluster0.5oywn.mongodb.net/ProyectoFinal?retryWrites=true")
mydb = myclient["ProyectoFinal"]

myquery = {"metadata.iso_language_code" : "en"}
myselect = {"text" : 1, "_id" : 0}

row_list = [["text", "sentiment"]]

def Negative():
    global row_list
    mycol = mydb["Negative"]
    mydoc = mycol.find(myquery, myselect).limit(10000)
    for x in mydoc:
        row_list.append([x['text'], 0])

def Positive():
    global row_list
    mycol = mydb["Positive"]
    mydoc = mycol.find(myquery, myselect).limit(10000)
    for x in mydoc:
        row_list.append([x['text'], 1])

Negative()
Positive()

with open('dataTwitter.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)
