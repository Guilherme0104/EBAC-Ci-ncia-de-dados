import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv(r"C:\Users\luisx\OneDrive\Área de Trabalho\EBAC\clientes-v3-preparado.csv")

print(df.head(50))

plt.hist(df['salario'])
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(df['salario'], bins=100, color='green', alpha=0.8)
plt.title("Histograma - Distribuição de salarios")
plt.xlabel("Salario")
plt.xticks(ticks=range(0,int(df["salario"].max())+2000, 2000))
plt.ylabel("Frequencia")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.subplot(2,2,1)
plt.scatter(df["salario"], df["salario"])
plt.title("Dispersão - Salario e Salario")
plt.xlabel('Salario')
plt.ylabel("Salario")

plt.subplot(1,2,2)
plt.scatter(df["idade"], df['anos_experiencia'], color='#5882a8', alpha=0.6, s=30)
plt.title("Dispersão - Idade e Anos de experiencia")
plt.xlabel('Salario')
plt.ylabel('Anos de experiencia')

corr = df[['salario', 'anos_experiencia']].corr()
plt.subplot(2,2,3)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Salario e Idade')

plt.tight_layout()
plt.show()