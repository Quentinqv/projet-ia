import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Données extraites du notebook
# Répartition des classes
class_distribution = {'Not Spam': 39595, 'Spam': 42891}  # Exemple, remplacez par les vraies valeurs

# Rapport de classification (extrait du notebook)
classification_report_dict = {
    'Not Spam': {'precision': 0.96, 'recall': 0.99, 'f1-score': 0.98, 'support': 7962},
    'Spam': {'precision': 0.99, 'recall': 0.98, 'f1-score': 0.98, 'support': 8536},
    'accuracy': 0.98,
    'macro avg': {'precision': 0.98, 'recall': 0.98, 'f1-score': 0.98, 'support': 16498},
    'weighted avg': {'precision': 0.98, 'recall': 0.98, 'f1-score': 0.98, 'support': 16498}
}

# Matrice de confusion
conf_mat = [
    [7885, 16],
    [42, 8555]
]

# Hyperparamètres optimaux
best_params = {'randomforestclassifier__max_depth': None, 'randomforestclassifier__n_estimators': 100}


def show():
    st.title("Performance du modèle")

    st.header("Distribution des classes")
    class_df = pd.DataFrame(list(class_distribution.items()), columns=['Class', 'Count'])
    st.bar_chart(class_df.set_index('Class'))

    st.header("Rapport de classification")
    report_df = pd.DataFrame(classification_report_dict).transpose()
    st.dataframe(report_df)

    st.header("Matrice de confusion")
    plt.figure(figsize=(10, 7))
    sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues', xticklabels=['Not Spam', 'Spam'],
                yticklabels=['Not Spam', 'Spam'])
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Matrice de confusion')
    st.pyplot(plt)

    st.header("Meilleurs hyperparamètres")
    # Expliquer ce que sont les hyperparamètres et pourquoi ils sont importants
    st.write("Les hyperparamètres sont des paramètres que vous devez définir avant d'entraîner un modèle. "
             "Ils affectent la performance du modèle et doivent être choisis avec soin. "
             "Les hyperparamètres optimaux trouvés pour ce modèle sont:")
    st.write(best_params)

    # Show two images in assets folder to display a wordcloud of spam and not spam emails
    st.header("Nuages de mots")
    col1, col2 = st.columns(2)
    with col1:
        st.image("assets/wordcloud_spam.png", use_column_width=True)
        st.write("Nuage de mots des emails Spam")
    with col2:
        st.image("assets/wordcloud_non_spam.png", use_column_width=True)
        st.write("Nuage de mots des emails non Spam")
