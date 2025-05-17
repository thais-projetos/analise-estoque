import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do estoque
estoque = pd.read_csv("estoque.csv")

# Exibir resumo
print("Resumo do estoque:\n")
print(estoque.describe())
print("\nProdutos com baixo estoque (menos de 20 unidades):")
print(estoque[estoque["Quantidade"] < 20])

# Gerar gráfico
plt.figure(figsize=(10, 6))
plt.bar(estoque["Produto"], estoque["Quantidade"], color="skyblue")
plt.title("Quantidade em Estoque por Produto")
plt.xlabel("Produto")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)
plt.tight_layout()

# Salvar gráfico corretamente
plt.savefig("grafico_estoque.png", bbox_inches='tight')
plt.close()

print("\nGráfico salvo como 'grafico_estoque.png'")
