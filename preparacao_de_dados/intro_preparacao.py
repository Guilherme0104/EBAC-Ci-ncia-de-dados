import pandas as pd

df = pd.read_csv(r'C:\Users\luisx\OneDrive\Área de Trabalho\EBAC\clientes-v2.csv')

pd.set_option('display.max_columns', None)

print(df.head().to_string())
print(df.tail().to_string())

df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

print(f'Verificação inicial:\n{df.info()}')


print(f'Analise de dados nulos: \n{df.isnull().sum()}')
print(f'% de dados nulos: \n{df.isnull().mean() * 100}')
df.dropna(inplace=True)
print(f'confirmar remoção de nulos:\n{df.isnull().sum()}')

print(f'Confirmar remoção de dados nulos:\n{df.isnull().sum().sum()}')

print(f'analise de dados duplicados:\n{df.duplicated().sum()}')

print(f'analise de dados unicos:\n{df.nunique()}')

print(f'estatistica de dados:\n{df.describe()}')

df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]

print(df.head().to_string())

df.to_csv('clientes-v2-tratados.csv', index=False)