import streamlit as st

def app():
    st.title("Você viu meu pet?")    
    st.write("""
        Encontre seu pet perdido com facilidade! Nossa plataforma conecta tutores e pets desaparecidos de forma rápida e segura, reunindo informações úteis e permitindo reencontros emocionantes. Junte-se a nós e traga seu amigo de volta para casa!
    """)

    # Estilizando com CSS
    footer = """
    <style>
    footer {
        visibility: hidden;
    }
    .custom-footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 10px;
        text-align: right; 
        background-color: rgb(38, 39, 48, 0.31);
        font-size: 8px;
        line-height: 10px;
        color: rgb(250, 250, 250);
        word-break: break-word;
    }
    </style>

    <div class="custom-footer">
        <p>Aplicação web elaborada durante a disciplina de extensão do curso de Análise e Desenvolvimento de Sistemas da Unifil</p> 
        <p>Desenvolvido por Nicolas Ruiz | Rachell Tahuny | © 2023-2024</p>
    """

    # Injetando o CSS e HTML no app
    st.markdown(footer, unsafe_allow_html=True)
