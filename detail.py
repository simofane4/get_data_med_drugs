from unittest import expectedFailure
from bs4 import BeautifulSoup
import requests
import json
import os




def append_to_json(_dict,path): 
    with open(path, 'ab+') as f:
        f.seek(0,2)                                #Go to the end of file    
        if f.tell() == 0 :                         #Check if file is empty
            f.write(json.dumps([_dict]).encode())  #If empty, write an array
        else :
            f.seek(-1,2)           
            f.truncate()                           #Remove the last character, open the array
            f.write(' , '.encode())                #Write the separator
            f.write(json.dumps(_dict).encode())    #Dump the dictionary
            f.write(']'.encode())                  #Close the array



def get_detail(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.content,"html.parser")
    rdiv= soup.find('div', class_='single-medicament')
    name = rdiv.find('h3').getText()
    try:
        presentation = rdiv.find('tr', class_='field-presentation').find('td', class_='value').getText()
    except AttributeError : 
        presentation = None
    try:
        dosage = rdiv.find('tr', class_='field-dosage').find('td', class_='value').getText()
    except  AttributeError:
        dosage = None
    try: 
        distributeur = rdiv.find('tr', class_='field-distributeur').find('td', class_='value').getText()
    except AttributeError:
        distributeur = None
    try: 
        composition = rdiv.find('tr', class_='field-composition').find('td', class_='value').getText()
    except AttributeError : 
        composition = None
    try: 
        famille = rdiv.find('tr', class_='field-famille').find('td', class_='value').getText()
    except AttributeError : 
        famille = None
    try: 
        statut = rdiv.find('tr', class_='field-statut').find('td', class_='value').getText()
    except AttributeError :
        statut = None
    try:
        atc = rdiv.find('tr', class_='field-atc').find('td', class_='value').getText()
    except AttributeError: 
        atc = None
    try:
        ppv = rdiv.find('tr', class_='field-ppv').find('td', class_='value').getText()
    except AttributeError : 
        ppv = None
    try: 
        prix_hospitalier = rdiv.find('tr', class_='field-prix_hospitalier').find('td', class_='value').getText()
    except AttributeError : 
        prix_hospitalier = None
    try:
        pph =  rdiv.find('tr', class_='field-pph').find('td', class_='value').getText()
    except  AttributeError:
        pph = None
    try:
        tableau =  rdiv.find('tr', class_='field-tableau').find('td', class_='value').getText()
    except AttributeError :
        tableau = None
    try: 
        indication = rdiv.find('tr', class_='field-indication').find('td', class_='value').getText()
    except AttributeError :
        indication = None 
    try:
        substance_psychoactive = rdiv.find('tr', class_='field-substance_psychoactive').find('td', class_='value').getText()
    except  AttributeError:
        substance_psychoactive = None
    object = {
        'name': name,
        'presentation':presentation,
        'dosage':dosage,
        'distributeur':distributeur,
        'composition':composition,
        'famille':famille,
        'statut':statut,
        'atc':atc,
        'ppv':ppv,
        'prix_hospitalier':prix_hospitalier,
        'pph':pph,
        'tableau':tableau,
        'indication':indication,
        'substance_psychoactive':substance_psychoactive
    }
    return object



