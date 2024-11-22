import streamlit as st
from app.pages import home, pets_perdidos, pets_encontrados, cadastro

# Dicionário de páginas
PAGES = {
    "Página Inicial": home,
    "Pets Perdidos": pets_perdidos,
    "Pets Encontrados": pets_encontrados,
    "Cadastro de Pets": cadastro
}

def main():
    st.sidebar.title("Navegação")
    choice = st.sidebar.radio("Ir para", list(PAGES.keys()))

    # Renderiza a página escolhida
    page = PAGES[choice]
    page.app()

if __name__ == "__main__":
    main()