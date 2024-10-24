import requests
from bs4 import BeautifulSoup

url = 'https://wiki.python.org.br/AprendaMais'

requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')


#print(extracao.text.strip())

# for linha_texto, texto in extracao.findAll('h2'):
#     titulo = linha_texto.text.strip()
    
#     print('titulo: ', titulo)
    

# conta_titulos = 0;
# conta_texto = 0

# for linha_texto in extracao.findAll(['h2','p']):
#     if linha_texto.name == 'h2':
#         conta_titulos += 1
#     elif linha_texto.name == 'p':
#         conta_texto += 1
    

# print(f'total de titulos: {conta_titulos}')
# print(f"total de paragrafos: {conta_texto}")


# for linha_texto in extracao.find_all(["h2", "p"]):
#     if linha_texto.name == 'h2':
#         titulo =linha_texto.text.strip()
#         print(f"titulo: \n{titulo}")
#     elif linha_texto.name == 'p':
#         paragrafo = linha_texto.text.strip()
#         print(f'paragrafo: \n{paragrafo}')
    
    
for titulo in extracao.findAll("h2"):
    print(f'\n Titulo: {titulo.text.strip()}')
    for link in titulo.find_next_siblings('p'):
        for a in link.findAll("a",href=True):
            print(f'texto link: {a.text.strip()} | URL:{a['href']}')