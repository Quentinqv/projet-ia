import streamlit as st


def show(model):
    st.title("Tester le modèle")
    st.write("Écrire le mail en anglais.")
    sender = st.text_input("Envoyeur")
    subject = st.text_input("Objet")
    body = st.text_area("Corps du mail")

    if st.button("Vérifier"):
        email_text = sender + ' ' + subject + ' ' + body
        prediction = model.predict([email_text])

        if prediction[0] == 1:
            st.markdown(
                """
                <div style="text-align: center;">
                    <h2 style="color: red;">🚫 Cet email est considéré comme un SPAM</h2>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """
                <div style="text-align: center;">
                    <h2 style="color: green;">✅ Cet email N'EST PAS considéré comme SPAM</h2>
                </div>
                """,
                unsafe_allow_html=True,
            )
