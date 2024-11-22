import os
import streamlit as st
from database.db_operations import fetch_approved_pets, debug_database

UPLOADS_DIR = os.path.abspath("uploads")

def app():
    st.title("Pets Perdidos")
    st.write("Aqui você encontra informações sobre pets perdidos em Londrina - PR")

    # Diagnóstico: verifica se a tabela existe
    debug_database()

    # Busca os pets perdidos aprovados
    try:
        pets_perdidos = fetch_approved_pets("Perdido")
    except Exception as e:
        st.error(f"Erro ao acessar o banco de dados: {e}")
        return

    if not pets_perdidos:
        st.info("Nenhum pet perdido foi cadastrado ou aprovado até o momento.")
        return

    # Exibe os pets perdidos aprovados
    for pet in pets_perdidos:
        with st.container():
            st.markdown("---")
            st.subheader(f"{pet['nomepet']}")
            st.write(f"**Tutor(a)**: {pet['nome']}")
            st.write(f"**Espécie**: {pet['especiepet']}")
            st.write(f"**Raça**: {pet['racapet']}")
            st.write(f"**Cor**: {pet['corpet']}")
            st.write(f"**Localização**: {pet['localizacaopet']}")
            st.write(f"**Última vez em que foi visto**: {pet['datapet']}")
            st.write(f"**Informações adicionais**: {pet['infoadicionalpet']}")
            st.write(f"**Contato**: {pet['telefone']}")
            
         # Caminho da imagem
        image_path = os.path.join(UPLOADS_DIR, pet["imagempet"])

        # Verifica se a imagem existe e exibe
        if os.path.exists(image_path):
            st.image(image_path, caption=f"Imagem do pet: {pet['nomepet']}")
        else:
            st.warning(f"Imagem não encontrada: {pet['imagempet']}")
        

            # Exibe a imagem do pet, se disponível
            # try:
            #     st.image(f"uploads/{pet['imagempet']}", caption=f"Imagem do pet: {pet['nomepet']}")
            # except FileNotFoundError:
            #     st.warning("Imagem não disponível.")










# import sqlite3
# import pandas as pd
# import streamlit as st

# def app():
#     st.title("Pets Perdidos")

#     # Conectar ao banco de dados SQLite
#     connection = sqlite3.connect("../pet_database")
#     cursor = connection.cursor()

#     # Consultar os pets perdidos
#     query = "SELECT * FROM cadastropet WHERE statuspet = 'Perdido'"
#     cursor.execute(query)

#     # Recuperar os dados
#     rows = cursor.fetchall()

#     # Fechar a conexão
#     connection.close()

#     if rows:
#         # Criar um DataFrame do pandas para exibir os dados como uma tabela
#         columns = [description[0] for description in cursor.description]
#         df = pd.DataFrame(rows, columns=columns)

#         # Exibir a tabela no Streamlit
#         st.write(df)
#     else:
#         st.write("Não há pets perdidos cadastrados no momento.")