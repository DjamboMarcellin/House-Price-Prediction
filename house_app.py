# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 20:55:59 2023

@author: djamb
"""

import streamlit as st
import pickle

#Charger le modele

model = pickle.load(open('random_forest_regression_model_house_pred.pkl','rb'))

#Focntion pour effectuer la prediction
def predict_prix(bedrooms, bathrooms, stories, mainroad, guestroom, basement,
       hotwaterheating, airconditioning, parking, prefarea,
       furnishingstatus):
    # Mapper le mainroad
    mainroad_map = {'Yes': 1, 'No': 0}
    mainroad = mainroad_map[mainroad]

    # Mapper le guestroom
    guestroom_map = {'No': 0, 'Yes': 1}
    guestroom = guestroom_map[guestroom]

    # Mapper le basement
    basement_map = {'Yes': 1, 'No': 0}
    basement = basement_map[basement]

    # Mapper le hotwaterheating
    hotwaterheating_map = {'Yes': 1, 'No': 0}
    hotwaterheating = hotwaterheating_map[hotwaterheating]

    # Mapper le airconditioning
    airconditioning_map = {'Yes': 1, 'No': 0}
    airconditioning = airconditioning_map[airconditioning]

    # Mapper le prefarea
    prefarea_map = {'Yes': 1, 'No': 0}
    prefarea = prefarea_map[prefarea]

    # Mapper le furnishingstatus
    furnishingstatus_map = {'Furnished': 0, 'Semi-Furnished': 1, 'Unfurnished': 2}
    furnishingstatus = furnishingstatus_map[furnishingstatus]

    # Effectuer la prédiction
    prediction = model.predict([[bedrooms, bathrooms, stories, mainroad, guestroom, basement,
           hotwaterheating, airconditioning, parking, prefarea,
           furnishingstatus]])

    return round(prediction[0], 2)


#Interface user

def main():
    st.title('House Price Prediction App')
    
    #Collecter les entrees de l'utilisateur
    
    bedrooms = st.number_input("Nombre de chambre",min_value = 0)
    bathrooms = st.number_input("Nombre de salle de bains", min_value=0)
    stories = st.number_input("Nombre d'étages", min_value=0)
    
    mainroad = st.radio("Accès à la route principale", ('Yes', 'No'))
    guestroom = st.radio("Chambre d'amis", ('Yes', 'No'))
    basement = st.radio("Sous-sol", ('Yes', 'No'))
    hotwaterheating = st.radio("Chauffe-eau", ('Yes', 'No'))
    airconditioning = st.radio("Climatisation", ('Yes', 'No'))
    
    parking = st.number_input("Nombre de places de parking", min_value=0)
    
    prefarea = st.radio("Zone préférée", ('Yes', 'No'))
    
    furnishingstatus = st.selectbox("Statut de l'ameublement", ('Furnished', 'Semi-Furnished', 'Unfurnished'))
    
    # Bouton pour effectuer la prédiction
    if st.button("Prédire le prix"):
        result = predict_prix(bedrooms, bathrooms, stories, mainroad, guestroom, basement,
                              hotwaterheating, airconditioning, parking, prefarea,
                              furnishingstatus)
        st.success(f"Le prix prédit de la maison est : {result} dollars")
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    