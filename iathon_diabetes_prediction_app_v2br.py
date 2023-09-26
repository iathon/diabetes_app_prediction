import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the trained Random Forest model
model = joblib.load('diabetes_prediction_sylhetdb_rf_model.pkl')

# Function to preprocess user input data
def preprocess_input(age, polyuria, polydipsia, sudden_weight_loss, polyphagia, visual_blurring,
                     irritability, delayed_healing, alopecia, peso, altura):

    # Calculate BMI and classify obesity as 1 (obese) or 0 (not obese)
    altura_metros = altura / 100
    bmi = peso / (altura_metros ** 2)
    obesity = 1 if bmi >= 30 else 0

    # Create a DataFrame with the user input
    user_data = pd.DataFrame({
        'idade': [age],
        'poliuria': [polyuria],
        'polidipsia': [polydipsia],
        'perda_peso_repentina': [sudden_weight_loss],
        'polifagia': [polyphagia],
        'visao_embacada': [visual_blurring],
        'irritabilidade': [irritability],
        'cicatrizacao_lenta': [delayed_healing],
        'alopecia': [alopecia],
        'obesidade': [obesity]
    })

    return user_data

# Streamlit app
def main():
    st.title("Aplicativo de Previsão de Diabetes")

    # User input form
    st.header("Informações do Usuário")
    age = st.slider("Idade", 0, 100, 30)
    polyuria = st.checkbox("Poliúria", help="Produção excessiva de urina")
    polydipsia = st.checkbox("Polidipsia", help="Sede excessiva")
    sudden_weight_loss = st.checkbox("Perda de Peso Repentina", help="Perda significativa de peso sem motivo aparente")
    polyphagia = st.checkbox("Polifagia", help="Aumento anormal do apetite")
    visual_blurring = st.checkbox("Visão Embaçada", help="Visão embaçada ou turva")
    irritability = st.checkbox("Irritabilidade", help="Alterações frequentes de humor")
    delayed_healing = st.checkbox("Cicatrização Lenta", help="Feridas que demoram a cicatrizar")
    alopecia = st.checkbox("Alopecia", help="Perda de cabelo")
    peso = st.number_input("Peso (kg)", 0.0)
    altura = st.number_input("Altura (cm)", 0.0)

    if st.button("Prever"):
        # Preprocess user input
        user_data = preprocess_input(age, polyuria, polydipsia, sudden_weight_loss, polyphagia, visual_blurring,
                     irritability, delayed_healing, alopecia, peso, altura)

        # Make a prediction
        prediction = model.predict_proba(user_data)[:, 1]

        st.header("Resultado da Previsão")
      if prediction == 1:
        st.write(f"Você tem altas chances de ter ou vir a desenvolver diabetes")
      else:
        st.write(f"Você tem baixas chances de ter diabetes")
        

if __name__ == '__main__':
    main()


# In[ ]:




