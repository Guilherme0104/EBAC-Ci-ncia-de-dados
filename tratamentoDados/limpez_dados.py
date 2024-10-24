import pandas as pd


df = pd.read_csv(r'C:\Users\luisx\OneDrive\Área de Trabalho\EBAC\tratamentoDados\clientes.csv')
pd.set_option('display.width', None)
print(df.head)

df.drop('pais', axis=1, inplace=True)
df.drop(2, axis=0,  inplace=True)

df['nome'] = df['nome'].str.title()
df['endereco'] = df['endereco'].str.lower()
df['estado'] = df['estado'].str.strip().str.upper()



df['idade'] =  df['idade'].astype(int)


df_fillna = df.fillna(0)
df_dropna = df.dropna()
df_dropna4 = df.dropna(thresh=4)
df = df.dropna(subset=['cpf'])

print(f'Valors nulos: \n{df.isnull().sum()}')
print(f'Qtd de registros nulos com fillna: {df_fillna.isnull().sum().sum()}')
print(f'Qtd de registros nulos com dropna: {df_dropna.isnull().sum().sum()}')
print(f'Qtd de registros nulos com dropna4: {df_dropna4.isnull().sum().sum()}')
print(f'Qtd de registros nulos com CPF: {df.isnull().sum().sum()}')

df.fillna({'estado': 'desconhecido'},inplace=True)
df['endereco'] = df['endereco'].fillna('Endereço não informado')
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean())

df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

print(f'Qtd registro atual: {df.shape[0]}')
df.drop_duplicates()
df.drop_duplicates(subset='cpf', inplace=True)
print(f'Qtd registros removendo as duplicadas: {len(df)}')

print(f'Dados lmpos\n{df}')

df['data'] = df['data_corrigida']
df['idade'] = df['idade_corrigida']

df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'estado']]
df_salvar.to_csv('clientes_limpeza.csv', index=False)

print(f'Novo DataFrame:\n{pd.read_csv('clientes_limpeza.csv')}')