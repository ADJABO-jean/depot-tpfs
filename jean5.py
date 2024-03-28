#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Importation des modules 
import pandas as pd
import mysql.connector
from mysql.connector import Error

#Chargement des données
winequality-white = pd.read_excel("C:\Users\LAB-MND\Desktop\Nouveau dossier\wine+quality\winequality-white.csv")
print(winequality-white.columns)

colonnes = ['fixed acidity', 'volatile acidity', 'citric acidity', 'residual sugar','chlorides', 'free sulfur dioxide', 'total sulfur', 'density','pH','sulphates','alcohol','quality']
winequality-white.columns = colonnes 
print('----------------------------------------------------------------')
print(winequality-white.columns)

# Chargement du dataframe dans MYSQL
try:
    connexion = mysql.connector.connect(host='localhost',
                                       database='jean',
                                       user='root',
                                       password='')
    if connexion.is_connected():
        print('Connexion à MySQL réussie')
except Error as e:
    print(f"Erreur lors de la connexion à MySQL: {e}")

try:
    cursor = connexion.cursor()

    for i,row in winequality-white.iterrows():
        sql = """INSERT INTO culture_winequality-white (['fixed acidity', 'volatile acidity', 'citric acidity', 'residual sugar','chlorides', 'free sulfur dioxide', 'total sulfur', 'density','pH','sulphates','alcohol','quality']) VALUES   (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        #print(sql)
        cursor.execute(sql, tuple(row))

    connexion.commit()
    connexion.close()
    print("DataFrame chargé dans MySQL avec succès!")
except Exception as e:
    print(f"Erreur lors du chargement du DataFrame dans MySQL: {e}")




