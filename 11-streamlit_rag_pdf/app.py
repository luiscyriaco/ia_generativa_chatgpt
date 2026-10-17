import streamlit as st # cria a interface do usuário

def main():
    st.set_page_config(page_title='ChatbotPDF',page_icon=':books:')

    # Criar barra lateral esquerda da aplicação
    with st.sidebar:
        st.subheader("Seus Arquivos")
        pdf_docs=st.file_uploader("Carregar arquivos PDF",type="pdf",label_visibility="visible",accept_multiple_files=True)
        
        print(pdf_docs)
        
        if st.button('Processar'):
            pass


if __name__ == "__main__":
    main()


