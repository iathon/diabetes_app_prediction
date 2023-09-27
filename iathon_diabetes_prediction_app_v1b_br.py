import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load do modelo de ML
model = joblib.load('diabetes_prediction_sylhetdb_rf_model.pkl')

# função para pré-processar os dados de input
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
    
    
# configurar o layout do Streamlit
st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="✅",
    layout="wide",  # Set layout para wide, para fazer margens menores
)


# Streamlit app
def main():


    # aplicar custom CSS para minimizar margens da app para integração na página
    #pode não surtir efeito
    st.markdown(
    """
    <style>
    .stApp {
        margin-top: 0;
        margin-bottom: 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )
    
    # criar layout de 2 colunas
    column_widths = [1, 2]
    left_column, right_column = st.columns(column_widths)

    # colocar checkboxes à direita
    with right_column:
        poliuria = st.checkbox("Produção excessiva de urina", help="Poliúria")
        polidipsia = st.checkbox("Sede excessiva", help="Polidipsia")
        perda_peso_repentina = st.checkbox("Perda significativa de peso sem motivo aparente", help="Perda de Peso Repentina")
        polifagia = st.checkbox("Aumento anormal do apetite", help="Polifagia")
        visao_embacada = st.checkbox("Visão embaçada ou turva", help="Visão Embaçada")
        irritabilidade = st.checkbox("Alterações frequentes de humor", help="Irritabilidade")
        cicatrizacao_lenta = st.checkbox("Feridas que demoram a cicatrizar", help="Cicatrização Lenta")
        alopecia = st.checkbox("Perda de cabelo", help="Alopecia")
    
    # colocar numéricos à esquerda
    with left_column:
        idade = st.slider("Idade", 0, 100, 30)
        peso = st.number_input("Peso (kg)", 0.0, format="%0.1f", key="peso")
        altura = st.number_input("Altura (cm)", 0.0, format="%0.1f", key="altura")


    st.markdown(
    """
    <style>
    .st-eb {
        width: 20px !important; /* Adjust the width as needed */
    }
    </style>
    """,
    unsafe_allow_html=True,
    )


    if st.button("Prever"):
        # pre-processar input
        user_data = preprocess_input(idade, poliuria, polidipsia, perda_peso_repentina, polifagia, visao_embacada, irritabilidade, cicatrizacao_lenta, alopecia, peso, altura)

        # fazer predição
        prediction = model.predict(user_data)
        
        
        #informar resultado ao usuário
        st.header("Resultado da Previsão")
        if prediction == 1:
            st.write("O nosso modelo indica que você tem boas chances de desenvolver diabestes")
            st.write("É boa ideia falar com um humano. Fale com o seu médico que o aconselhará nos passos a seguir.")
        else:
            st.write("O nosso modelo não encontrou razões para grandes preocupações em relação à diabetes.")
            st.write("Em qualquer caso, sempre acompanhe a sua saúde junto de profissionais qualificados.")

if __name__ == '__main__':
    main()

