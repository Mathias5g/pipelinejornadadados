import streamlit as st
from datetime import datetime, time
from contrato import Venda
from pydantic import ValidationError
from database import salvar_no_postgres

def main():
    st.title("CRM BMG")
    email = st.text_input("E-mail do vendedor")
    nome = st.text_input("Nome do vendedor")
    data = st.date_input("Data da venda", datetime.now())
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    produto = st.selectbox("Produto Vendido", ["Consignado INSS", "Consignado Privado", "FGTS"])

    if st.button("Salvar"):
        try:
            venda = Venda(email = email, nome = nome, data = data, valor = valor, produto = produto)
            st.write(venda)
            salvar_no_postgres(venda)
        except ValidationError as e:
            st.error(f"Erro: {e}")

        # st.write("**Dados da venda:**")
        # st.write(f"E-mail do vendedor: {email}")
        # st.write(f"Nome do vendedor: {nome}")
        # st.write(f"Data da venda: {data}")
        # st.write(f"Valor da venda: {valor}")
        # st.write(f"Produto: {produto}")

if __name__ == '__main__':
    main()