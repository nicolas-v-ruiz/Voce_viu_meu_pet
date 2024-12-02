import streamlit as st
from database.db_operations import fetch_pending_pets, approve_pet, reject_pet, connect

def admin_page():
    st.title("Administração de Cadastros de Pets")
    st.write("Aprovar ou rejeitar cadastros de pets pendentes para publicação.")

    # Teste de conexão ao banco
    try:
        with connect() as conn:
            st.success("Conexão com o banco de dados bem-sucedida!")
    except FileNotFoundError as e:
        st.error(f"Erro: {str(e)}")
        return

    # Buscar pets pendentes
    pets_pendentes = fetch_pending_pets()

    if not pets_pendentes:
        st.info("Nenhum cadastro pendente no momento.")
        return

    # Exibir cada pet pendente
    for pet in pets_pendentes:
        pet_id = pet['rowid']
        nomepet = pet['nomepet']
        especiepet = pet['especiepet']
        racapet = pet['racapet']
        corpet = pet['corpet']
        localizacaopet = pet['localizacaopet']
        datapet = pet['datapet']
        infoadicionalpet = pet['infoadicionalpet']
        imagempet = pet['imagempet']
        statuspet = pet['statuspet']

        with st.expander(f"{nomepet} - {statuspet}"):
            st.write(f"**Espécie:** {especiepet}")
            st.write(f"**Raça:** {racapet}")
            st.write(f"**Cor:** {corpet}")
            st.write(f"**Localização:** {localizacaopet}")
            st.write(f"**Data:** {datapet}")
            st.write(f"**Informações adicionais:** {infoadicionalpet}")
            if imagempet:
                st.image(f"uploads/{imagempet}", use_column_width=True)
            else:
                st.write("Sem imagem disponível.")

            col1, col2 = st.columns(2)

            if col1.button(f"Aprovar {pet_id}", key=f"aprovar_{pet_id}"):
                approve_pet(pet_id)
                st.success(f"Pet {nomepet} aprovado com sucesso!")

            if col2.button(f"Rejeitar {pet_id}", key=f"rejeitar_{pet_id}"):
                reject_pet(pet_id)
                st.warning(f"Pet {nomepet} rejeitado com sucesso!")

if __name__ == "__main__":
    admin_page()
