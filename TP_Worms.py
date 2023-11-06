#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:34:58 2023

@author: hannahmetaireau
"""

import json 
import requests
import pandas as pd

# Lire le fichier Excel
excel_file = "Table_espece_UTF8_simplifie.xlsx"
sheet_name = "Espece_incomplet"
df = pd.read_excel(excel_file, sheet_name)

# Fonction pour avoir les données worms 
def get_worms_data(aphiaid):
    url = f"https://www.marinespecies.org/rest/AphiaRecordByAphiaID/{aphiaid}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    
# Parcourir les lignes
for index, row in df.iterrows():
    aphiaid = row['aphiaid_accepted']  # Colonne du Excel avec les AphiaID
    worms_data = get_worms_data(aphiaid)
    
    if worms_data:
        # Parcourir dynamiquement toutes les colonnes du DataFrame
        for column in df.columns:
            if column in worms_data:
                df.at[index, column] = worms_data[column]
    


# Enregistrer les modifications dans le fichier Excel d'origine
df.to_excel(excel_file, sheet_name=sheet_name, index=False)

