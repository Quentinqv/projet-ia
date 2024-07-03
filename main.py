import streamlit as st
from streamlit_option_menu import option_menu
import joblib


# Charger le modèle
def load_model():
    model_path = 'model/model_phishing.pkl'
    model = joblib.load(model_path)
    return model


model = load_model()

# Menu de navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",  # required
        options=["Accueil", "Performance", "Tester le modèle"],  # required
        icons=["house", "bar-chart-line", "envelope"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
    )

if selected == "Accueil":
    from pages_import import Home

    Home.show()

elif selected == "Performance":
    from pages_import import Performance

    Performance.show()

elif selected == "Tester le modèle":
    from pages_import import Test_Model

    Test_Model.show(model)
