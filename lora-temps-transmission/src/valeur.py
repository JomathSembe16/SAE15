import csv
import re
header = "TIteration,TBlock,TMessGen,TMessSend,TDisplay,TOA,Essai,TxPower,SF,Bandwith,CodingRate,Taille,".split(",")

dico = {}
liste_dico=[]

with open('fusion.csv',"r") as csvfile:
    reader = csv.DictReader(csvfile,delimiter=";")
    for row in reader:
        liste_dico.append(row)

def search_by(arg,liste):
    l = []
    for i in liste:
        l.append(i[arg])
    return l

def missing_val(data):
    missing=0
    for i in data:
        if i=="":
            missing+=1
    return missing



