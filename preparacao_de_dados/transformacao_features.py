import pandas as pd
import numpy as np
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv(r'C:\Users\luisx\OneDrive\Área de Trabalho\EBAC\clientes-v2-tratados.csv')

print(df.head())

df['salario_log'] = np.log1p(df["salario"])

print(f"\nDataFrame após transformação logaritmica no 'salario':\n{df.head()}")

df['salario_box_cox'], _ = stats.boxcox(df['salario'] + 1)

print(f"\nDataFrame após transformação Box-Cox no 'salario':\n{df.head()}")

estado_freq = df['estado'].value_counts()/ len(df)

df['estado_freq'] = df['estado'].map(estado_freq)

df["interacao_idade_filhos"] = df['idade'] * df['numero_filhos']

print(f"\nDataFrame após criação de interações entre 'idade' e 'numero de filhos':\n{df.head()}")

print(df.to_string())