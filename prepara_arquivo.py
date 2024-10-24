import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\luisx\OneDrive\Área de Trabalho\EBAC\clientes-v2-tratados.csv")

df['anos_experiencia'] = np.random.randint(0, 11,df.shape[0])

print(df)

df.to_csv("clientes-v3-preparado.csv", index=False)