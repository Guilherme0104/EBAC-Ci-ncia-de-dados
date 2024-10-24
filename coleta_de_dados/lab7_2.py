import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)
requisicao.encoding = 'utf-8'

extracao = BeautifulSoup(requisicao.text, 'html.parser')

contar_livros = 0
catalogo = []

for artigo in extracao.find_all('article', class_='product_pod'):
    livro = {}
    for head in artigo.find_all('h3'):
        titulo = head.text.strip()
        livro['Título'] = titulo
    for texto in artigo.find_all('p',class_='price_color'):
        preco = texto.text.strip()
        livro['Preço'] = preco
    catalogo.append(livro)

print('Total livros:', contar_livros)

for produto in catalogo:
    print(produto)