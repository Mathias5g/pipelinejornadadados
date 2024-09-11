import psycopg2
from psycopg2 import sql
from contrato import Venda
import streamlit as st
from dotenv import load_dotenv
import os

# Carregar variaveis do arquivo .env
load_dotenv()

# Configuração do banco de dados PostgreSQL
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

# Função para salvar os dados validos no PostgreSQL
def salvar_no_postgres(dados: Venda):
    """"
    Função pra salvar no banco de dados PostgreSQL
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cur = conn.cursor()

        # Inserção de dados na tabela de vendas
        insert_query = sql.SQL(
            "INSERT INTO vendas (email, nome, data, valor, produto) VALUES (%s, %s, %s, %s, %s)"
        )
        cur.execute(insert_query, (
            dados.email,
            dados.nome,
            dados.data,
            dados.valor,
            dados.produto.value
        ))
        conn.commit()
        cur.close()
        conn.close()
        st.success('Venda salva com sucesso!')
    except Exception as e:
        st.error(e)