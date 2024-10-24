import pandas as pd
from scipy import stats

pd.set_option('display.width', None )

df = pd.read_csv(r'C:\Users\luisx\OneDrive\Área de Trabalho\EBAC\tratamentoDados\clientes_limpeza.csv')

df_filtro_basico = df[df['idade']>100]

print(f'filtro basico:\n{df_filtro_basico[['nome','idade']]}')


z_scores = stats.zscore(df['idade'].dropna())
outliers_z = df[z_scores >= 3]  

print(f"outlier pelo Z-score:\n{outliers_z}")

df_zscore = df[(stats.zscore(df['idade']) < 3)]

Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = 18
limite_alto = 100

print(f'limite IQR: {limite_alto}, :{limite_baixo}')


outliers_iqr = df[(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)]
print(f"Outliers pelo IQR: \n{outliers_iqr}")


df_iqr = df[(df["idade"] >= limite_baixo) & (df['idade'] <= limite_alto)]



df['endereco'] = df['endereco'].apply(lambda x: 'endereço invalido' if len(x.split('/n')) < 3 else x)

df['nome'] = df['nome'].apply(lambda x: 'nome invalido' if isinstance(x, str) and len(x) > 50 else x)
print(f'Qtd registros com nomes grandes: {(df["nome"] =="nome invalido").sum()}')


print(f"Dados outliers tratados\n{df}")

df.to_csv("clientes_remove_outliers.csv", index= False)

