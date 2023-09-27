#!/usr/bin/env python
# coding: utf-8

# import streamlit as st
# import pandas as pd
# import joblib
# from sklearn.preprocessing import LabelEncoder
# 
# # Load the trained Random Forest model
# model = joblib.load('diabetes_prediction_sylhetdb_rf_model.pkl')
# 
# # Define a dictionary to map gender values to 0 (male) and 1 (female)
# gender_mapping = {'Masculino': 0, 'Feminino': 1}
# 
# # Function to preprocess user input data
# def preprocess_input(idade, genero, poliuria, polidipsia, perda_peso_repentina, polifagia, visao_embacada, irritabilidade, cicatrizacao_lenta, alopecia, obesidade):
#     # Encode gender
#     genero_codificado = gender_mapping[genero]
# 
#     # Create a DataFrame with the user input
#     user_data = pd.DataFrame({
#         'idade': [idade],
#         'genero': [genero_codificado],
#         'poliuria': [poliuria],
#         'polidipsia': [polidipsia],
#         'perda_peso_repentina': [perda_peso_repentina],
#         'polifagia': [polifagia],
#         'visao_embacada': [visao_embacada],
#         'irritabilidade': [irritabilidade],
#         'cicatrizacao_lenta': [cicatrizacao_lenta],
#         'alopecia': [alopecia],
#         'obesidade': [obesidade]
#     })
# 
#     return user_data
# 
# # Streamlit app
# def main():
#     st.title("Aplicativo de Previsão de Diabetes")
# 
#     # User input form
#     st.header("Informações do Usuário")
#     idade = st.slider("Idade", 0, 100, 30)
#     genero = st.selectbox("Gênero", ("Masculino", "Feminino"))
#     poliuria = st.checkbox("Poliúria")
#     polidipsia = st.checkbox("Polidipsia")
#     perda_peso_repentina = st.checkbox("Perda de Peso Repentina")
#     polifagia = st.checkbox("Polifagia")
#     visao_embacada = st.checkbox("Visão Embaçada")
#     irritabilidade = st.checkbox("Irritabilidade")
#     cicatrizacao_lenta = st.checkbox("Cicatrização Lenta")
#     alopecia = st.checkbox("Alopecia")
#     obesidade = st.checkbox("Obesidade")
# 
#     if st.button("Prever"):
#         # Preprocess user input
#         user_data = preprocess_input(idade, genero, poliuria, polidipsia, perda_peso_repentina, polifagia, visao_embacada, irritabilidade, cicatrizacao_lenta, alopecia, obesidade)
# 
#         # Make a prediction
#         prediction = model.predict_proba(user_data)[:, 1]
# 
#         st.header("Resultado da Previsão")
#         st.write(f"Probabilidade de desenvolver diabetes: {prediction[0]:.2f}")
# 
# if __name__ == '__main__':
#     main()
# 

# In[1]:


import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the trained Random Forest model
model = joblib.load('diabetes_prediction_sylhetdb_rf_model.pkl')

# Function to preprocess user input data
def preprocess_input(idade, poliuria, polidipsia, perda_peso_repentina, polifagia, visao_embacada, irritabilidade, cicatrizacao_lenta, alopecia, peso, altura):
    # Calculate BMI and classify obesity as 1 (obese) or 0 (not obese)
    altura_metros = altura / 100
    bmi = peso / (altura_metros ** 2)
    obesidade = 1 if bmi >= 30 else 0

    # Create a DataFrame with the user input
    user_data = pd.DataFrame({
        'idade': [idade],
        'poliuria': [poliuria],
        'polidipsia': [polidipsia],
        'perda_peso_repentina': [perda_peso_repentina],
        'polifagia': [polifagia],
        'visao_embacada': [visao_embacada],
        'irritabilidade': [irritabilidade],
        'cicatrizacao_lenta': [cicatrizacao_lenta],
        'alopecia': [alopecia],
        'obesidade': [obesidade]
    })

    return user_data


# Streamlit app
def main():
    st.title("Teste a sua probabilidade para desenvolver Diabetes")
    st.write("Com alguns poucos dados seus, o nosso modelo de IA vai calcular as suas chances de ter diabetes.")
    st.write("Experimente e tranquilize-se!")

    # User input form
    st.header("Informações do Usuário")
    idade = st.slider("Idade", 0, 100, 30)
    poliuria = st.checkbox("Poliúria", help="Produção excessiva de urina")
    polidipsia = st.checkbox("Polidipsia", help="Sede excessiva")
    perda_peso_repentina = st.checkbox("Perda de Peso Repentina", help="Perda significativa de peso sem motivo aparente")
    polifagia = st.checkbox("Polifagia", help="Aumento anormal do apetite")
    visao_embacada = st.checkbox("Visão Embaçada", help="Visão embaçada ou turva")
    irritabilidade = st.checkbox("Irritabilidade", help="Alterações frequentes de humor")
    cicatrizacao_lenta = st.checkbox("Cicatrização Lenta", help="Feridas que demoram a cicatrizar")
    alopecia = st.checkbox("Alopecia", help="Perda de cabelo")
    peso = st.number_input("Peso (kg)", 0.0)
    altura = st.number_input("Altura (cm)", 0.0)

    if st.button("Prever"):
        # Preprocess user input
        user_data = preprocess_input(idade, poliuria, polidipsia, perda_peso_repentina, polifagia, visao_embacada, irritabilidade, cicatrizacao_lenta, alopecia, peso, altura)

        # Make a prediction
        prediction = model.predict(user_data)

        st.header("Resultado da Previsão")
        if prediction == 1:
            st.write("O nosso modelo indica que você tem boas chances de desenvolver diabestes")
            st.write("É boa ideia falar com um humano. Fale com o seu médico que o aconselhará nos passos a seguir.")
        else:
            st.write("O nosso modelo não encontrou razões para grandes preocupações em relação à diabetes.")
            st.write("Em qualquer caso, sempre acompanhe a sua saúde junto de profissionais qualificados.")

if __name__ == '__main__':
    main()


# In[ ]:




