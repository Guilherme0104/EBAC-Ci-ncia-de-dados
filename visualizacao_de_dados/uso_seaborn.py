import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv(r"C:\Users\luisx\OneDrive\Área de Trabalho\EBAC\clientes-v3-preparado.csv")
print(df.head().to_string())

sns.jointplot(x='idade', y="salario", data=df, kind="scatter")
plt.show()

plt.figure(figsize=(10, 6))
sns.kdeplot(df['salario'], fill=True, color='#545422')
plt.title("Densidade de salario")
plt.xlabel("Salario")
plt.show()

sns.pairplot(df[['idade', 'salario', 'anos_experiencia', 'nivel_educacao']])
plt.show()

sns.regplot(x='idade', y='salario', data=df, color="#378456", scatter_kws={'alpha':0.5, 'color': '#aa2214'})
plt.title('Regressão de salario por idade')
plt.xlabel('Idade')
plt.ylabel("Salario")
plt.show()

sns.countplot(x="estado_civil", hue="nivel_educacao", data=df, palette="pastel")
plt.xlabel('Estado civil')
plt.ylabel('Nivel de educação')
plt.legend(title="Nivel de educação")
plt.show()