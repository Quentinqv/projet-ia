import streamlit as st
import pandas as pd


def show():
    st.title("Projet de détection de spam")
    st.write("""
    ## Introduction
    Ce projet utilise le Machine Learning et le traitement du langage naturel (NLP) pour détecter les emails de spam. L'objectif est de prédire si un email est un spam ou non en se basant sur son contenu textuel.

    ## Objectifs
    - Utiliser des techniques de NLP pour traiter les données textuelles des emails.
    - Entraîner un modèle de classification pour distinguer les spams des emails légitimes.
    - Évaluer les performances du modèle à l'aide de diverses métriques.
    - Visualiser les résultats et permettre aux utilisateurs de tester le modèle avec leurs propres emails.

    ## Méthodologie
    1. **Chargement des données** : Les emails sont chargés depuis un fichier CSV contenant le texte des emails et les étiquettes indiquant si l'email est un spam ou non.
    2. **Prétraitement des données** : Le texte des emails est directement utilisé sans nettoyage supplémentaire car ils sont déjà propres dans le fichier CSV.
    3. **Entraînement du modèle** : Un modèle de classification est entraîné en utilisant des techniques de vectorisation de texte comme TF-IDF et des algorithmes de Machine Learning tels que Naive Bayes et RandomForest.
    4. **Évaluation du modèle** : Les performances du modèle sont évaluées à l'aide de métriques telles que l'accuracy, le rappel, la précision.
    5. **Visualisation** : Les résultats sont visualisés sous forme de matrices de confusion et de nuages de mots.

    ## Fonctionnalités de l'application
    - **Accueil** : Présentation du projet et des objectifs.
    - **Performance du modèle** : Affichage des métriques de performance et des visualisations.
    - **Tester le modèle** : Permettre aux utilisateurs de tester le modèle en entrant leurs propres emails et voir si le modèle les classifie comme spam.

    ## Utilisation
    - Utilisez la barre de navigation sur le côté pour naviguer entre les différentes sections de l'application.
    - Allez à la section **Performance du modèle** pour voir comment le modèle se comporte sur les données de test.
    - Allez à la section **Tester le modèle** pour entrer un email et vérifier si le modèle le classe comme spam.

    Nous espérons que ce projet vous aidera à mieux comprendre comment les techniques de NLP et de Machine Learning peuvent être appliquées à la détection de spam.
    """)

    st.header("Aperçu des données")
    df = pd.read_csv("data/phishing_email.csv")
    st.dataframe(df.head(10))

