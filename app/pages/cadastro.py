import streamlit as st
from pathlib import Path
from database.db_operations import create_table, insert_pet
from helpers.image_processing import process_image

# Configura o diretório absoluto para uploads
UPLOADS_DIR = Path("C:/Users/FN84/OneDrive - PETROBRAS/Área de Trabalho/VoceViumeuPet - CRUD/projeto/uploads")
UPLOADS_DIR.mkdir(parents=True, exist_ok=True)  # Garante que o diretório existe

def app():
    # Garante a criação da tabela e atualização do esquema
    create_table()

    st.title("Cadastro de Pets")
    st.write("Preencha o formulário abaixo para cadastrar um pet perdido ou encontrado.")

    with st.form("cadastro_form"):
        nome = st.text_input("Seu nome")
        telefone = st.text_input("Seu telefone", placeholder="(DDD) XXXXX-XXXX")
        email = st.text_input("Seu email")
        nome_pet = st.text_input("Nome do Pet")
        status = st.selectbox("Status do Pet", ["Perdido", "Encontrado"])
        especie = st.selectbox("Espécie do Pet", ["Cão", "Gato"])
        raca = st.text_input("Raça do Pet")
        cor = st.text_input("Cor do Pet")
        localizacao = st.text_input("Localização")
        data = st.date_input("Data do evento")
        info_adicional = st.text_area("Informações adicionais")
        imagem = st.file_uploader("Carregar imagem do Pet", type=["jpg", "jpeg", "png"])
        enviar = st.form_submit_button("Cadastrar")

        if enviar:
            try:
                # Processa a imagem e salva no diretório absoluto
                image_name = process_image(imagem, {"nomepet": nome_pet, "datapet": str(data)})

                # Mostra sucesso do processamento da imagem
                st.success(f"Imagem processada com sucesso. Nome do arquivo: {image_name}")

                # Dados para inserção no banco
                pet_data = {
                    "nome": nome,
                    "telefone": telefone,
                    "email": email,
                    "nomepet": nome_pet,
                    "statuspet": status,
                    "especiepet": especie,
                    "racapet": raca,
                    "corpet": cor,
                    "localizacaopet": localizacao,
                    "datapet": str(data),
                    "infoadicionalpet": info_adicional,
                    "imagempet": image_name  # Salva o nome do arquivo no banco
                }

                # Insere os dados no banco
                insert_pet(pet_data)
                st.success("Pet cadastrado com sucesso!")
                
                # update_table_schema()

            except ValueError as e:
                st.error(f"Erro de validação: {e}")

            except RuntimeError as e:
                st.error(f"Erro ao processar a imagem: {e}")



# import streamlit as st
# from pathlib import Path
# from database.db_operations import create_table, insert_pet, update_table_schema
# from helpers.image_processing import process_image

# # Configura o diretório absoluto para uploads
# UPLOADS_DIR = Path("C:/Users/FN84/OneDrive - PETROBRAS/Área de Trabalho/VoceViumeuPet - CRUD/projeto/uploads")
# UPLOADS_DIR.mkdir(parents=True, exist_ok=True)  # Garante que o diretório existe

# def app():
#     # Garante a criação da tabela e atualização do esquema
#     create_table()
#     update_table_schema()

#     st.title("Cadastro de Pets")
#     st.write("Preencha o formulário abaixo para cadastrar um pet perdido ou encontrado.")

#     with st.form("cadastro_form"):
#         nome = st.text_input("Seu nome")
#         telefone = st.text_input("Seu telefone", placeholder="(DDD) XXXXX-XXXX")
#         email = st.text_input("Seu email")
#         nome_pet = st.text_input("Nome do Pet")
#         status = st.selectbox("Status do Pet", ["Perdido", "Encontrado"])
#         especie = st.selectbox("Espécie do Pet", ["Cão", "Gato"])
#         raca = st.text_input("Raça do Pet")
#         cor = st.text_input("Cor do Pet")
#         localizacao = st.text_input("Localização")
#         data = st.date_input("Data do evento")
#         info_adicional = st.text_area("Informações adicionais")
#         imagem = st.file_uploader("Carregar imagem do Pet", type=["jpg", "jpeg", "png"])
#         enviar = st.form_submit_button("Cadastrar")

#         if enviar:
#             try:
#                 # Processa a imagem e salva no diretório absoluto
#                 image_name = process_image(imagem, {"nomepet": nome_pet, "datapet": str(data)})
                
#                 # Mostra sucesso do processamento
#                 st.success(f"Imagem processada com sucesso. Nome do arquivo: {image_name}")

#                 # Dados para inserção no banco
#                 pet_data = {
#                     "nome": nome,
#                     "telefone": telefone,
#                     "email": email,
#                     "nomepet": nome_pet,
#                     "statuspet": status,
#                     "especiepet": especie,
#                     "racapet": raca,
#                     "corpet": cor,
#                     "localizacaopet": localizacao,
#                     "datapet": str(data),
#                     "infoadicionalpet": info_adicional,
#                     "imagempet": image_name  # Salva o nome do arquivo, com extensão
#                 }

#                 # Insere os dados no banco
#                 insert_pet(pet_data)
#                 st.success("Pet cadastrado com sucesso!")

#             except ValueError as e:
#                 st.error(f"Erro de validação: {e}")

#             except RuntimeError as e:
#                 st.error(f"Erro ao processar a imagem: {e}")

