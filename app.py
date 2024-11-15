import requests
import streamlit as st


def buscar_letras(banda, musica):

    endpoint = (f"https://api.lyrics.ovh/v1/{banda}/{musica}")
    response = requests.get(endpoint)
    print(response.status_code)
    letra = response.json()["lyrics"] if response.status_code == 200 else ""
    return letra


st.image("https://i.imgur.com/SmktDIH.png")


st.title("Letras de musicas :sunglasses:")


banda = st.text_input("Digite o nome da banda: ",key="banda")
musica = st.text_input("Digite o nome da musica: ", key="musica")

pesquisar = st.button("Pesquisar", key="pesquisar")

if pesquisar:
    letra = buscar_letras(banda, musica)
    if letra:
        st.success("Encontramos a letra da sua musica!")
        st.text(letra)
    else:
        st.error("Infelizmento nao foi possivel encontrar a letra dessa musica")