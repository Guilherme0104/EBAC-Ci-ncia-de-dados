import pandas as pd

df = pd.read_csv(r'C:\Users\luisx\OneDrive\Área de Trabalho\EBAC\tratamentoDados\clientes.csv')

print(df.head().to_string())
print(df.tail().to_string())

print('Qtd: ',df.shape)

print("tipagem: \n",df.dtypes)

print('valores nulos: ', df.isnull().sum())