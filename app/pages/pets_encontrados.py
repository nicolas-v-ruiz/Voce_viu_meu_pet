import streamlit as st
from database.db_operations import fetch_approved_pets, debug_database
import os

UPLOADS_DIR = os.path.abspath("uploads")

def app():
    st.title("Pets Encontrados")
    st.write("Aqui você encontra informações sobre pets encontrados em Londrina - PR")

    # Diagnóstico: verifica se a tabela existe
    debug_database()

    # Busca os pets encontrados aprovados
    try:
        pets_encontrados = fetch_approved_pets("Encontrado")
    except Exception as e:
        st.error(f"Erro ao acessar o banco de dados: {e}")
        return

    if not pets_encontrados:
        st.info("Nenhum pet encontrado foi cadastrado ou aprovado até o momento.")
        return

    # Exibe os pets encontrados aprovados
    for pet in pets_encontrados:
        with st.container():
            st.markdown("---")
            st.subheader(f"{pet['nomepet']}")
            st.write(f"**Pessoa que encontrou**: {pet['nome']}")
            st.write(f"**Espécie**: {pet['especiepet']}")
            st.write(f"**Raça**: {pet['racapet']}")
            st.write(f"**Cor**: {pet['corpet']}")
            st.write(f"**Localização**: {pet['localizacaopet']}")
            st.write(f"**Foi encontrado em**: {pet['datapet']}")
            st.write(f"**Informações adicionais**: {pet['infoadicionalpet']}")
            st.write(f"**Contato**: {pet['telefone']}")

        image_path = os.path.join(UPLOADS_DIR, pet["imagempet"])

        # Verifica se a imagem existe e exibe
        if os.path.exists(image_path):
            st.image(image_path, caption=f"Imagem do pet: {pet['nomepet']}")
        else:
            st.warning(f"Imagem não encontrada: {pet['imagempet']}")