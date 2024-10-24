import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)

df = pd.read_csv(r'C:\Users\luisx\OneDrive\Área de Trabalho\EBAC\clientes-v2-tratados.csv')

print(df.head())

df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1)

print(f'\nDataFrame após a codificação one-hot para o "estado civil":\n{df.head()}')

educacao_ordem = {'Ensino Fundamental':1, "Ensino Médio":2, "Ensino Superior":3, 'Pós-graduação':4}
df['nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)

print(f"\nDataFrame após a codificação ordinal para 'nivel_educacao':\n{df.head()}")

df['area_atuacao_cod'] = df['area_atuacao'].astype('category').cat.codes

print(f"\nDataFrame após transformar 'area_atuacao' em codigos numericos:\n{df.head()}")

label_encoder = LabelEncoder()
df['estado_cod'] = label_encoder.fit_transform(df["estado"])

print(f"\nDataFrame após aplicar LabelEncoder em 'estado':\n{df.head()}")