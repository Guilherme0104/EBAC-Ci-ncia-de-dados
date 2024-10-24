import requests

def enviar_arquivo():
    
    caminho = r"C:\Users\luisx\Downloads\produtos_informatica.xlsx"
    
    requisicao = requests.post('https://file.io/', files={'file': open(caminho, 'rb')})
    saida_requsicao = requisicao.json()
    
    print(saida_requsicao)
    
    url = saida_requsicao['link']
    print(f'Arquivo enviado. Link para acesso: {url}')
    print(f"{type(requisicao)} {requisicao=}")

#CXHMUQ6.H3MQ7AK-0JE4QWN-MB6YKT2-S0D2AYS
def enviar_arquivo_chave():
    caminho = r"C:\Users\luisx\Downloads\produtos_informatica.xlsx"
    chave = 'CXHMUQ6.H3MQ7AK-0JE4QWN-MB6YKT2-S0D2AYS'
    
    requisicao = requests.post('https://file.io/', 
                               files={'file': open(caminho, 'rb')},
                               headers={'Authorization':chave})
    saida_requsicao = requisicao.json()
    print(saida_requsicao)
    


def receber_arquivo(file_url):
    requisicao = requests.get(file_url,)

    if requisicao.ok:
        with open('arquivo baxado.xlsx', "wb") as file:
            file.write(requisicao.content)
        print('arquivo baixado com sucesso')
    else:
        print("erro ao baixar arquivo",requisicao.json())



#enviar_arquivo()
#enviar_arquivo_chave()
receber_arquivo('https://file.io/IN5lSZ8pX8gA')