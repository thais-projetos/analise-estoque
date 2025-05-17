import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dados fictícios de estoque e vendas
estoque = pd.DataFrame({
    'produto_id': [101, 102, 103, 104, 105],
    'produto_nome': ['Mouse', 'Teclado', 'Monitor', 'Cadeira', 'Webcam'],
    'quantidade_estoque': [50, 20, 15, 5, 8],
    'estoque_minimo': [10, 10, 5, 5, 3]
})

vendas = pd.DataFrame({
    'produto_id': [101, 102, 101, 103, 104, 102, 105, 101, 104, 105, 103],
    'quantidade_vendida': [5, 2, 10, 3, 1, 5, 7, 8, 2, 4, 2]
})

# Passo 1: Calcular vendas totais por produto
vendas_totais = vendas.groupby('produto_id')['quantidade_vendida'].sum().reset_index()

# Passo 2: Unir estoque com vendas totais
dados = estoque.merge(vendas_totais, on='produto_id', how='left')
dados['quantidade_vendida'] = dados['quantidade_vendida'].fillna(0)

# Passo 3: Calcular giro de estoque = vendas / estoque disponível
dados['giro_estoque'] = dados['quantidade_vendida'] / dados['quantidade_estoque']

# Passo 4: Identificar produtos abaixo do estoque mínimo
dados['alerta_estoque_baixo'] = dados['quantidade_estoque'] <= dados['estoque_minimo']

print("Análise de Estoque:\n")
print(dados[['produto_nome', 'quantidade_estoque', 'quantidade_vendida', 'giro_estoque', 'alerta_estoque_baixo']])

# Visualizar estoque e vendas
plt.figure(figsize=(8,5))
sns.barplot(data=dados, x='produto_nome', y='quantidade_estoque', color='blue', label='Estoque')
sns.barplot(data=dados, x='produto_nome', y='quantidade_vendida', color='orange', label='Vendas')
plt.title('Estoque vs Vendas por Produto')
plt.ylabel('Quantidade')
plt.legend()
plt.show()
plt.savefig("estoque_baixo.png")  




# Recomendações simples
print("\nRecomendações:")
for _, row in dados.iterrows():
    if row['alerta_estoque_baixo']:
        print(f"- Repor estoque do produto '{row['produto_nome']}' (estoque atual: {row['quantidade_estoque']})")
    if row['giro_estoque'] < 0.1:
        print(f"- Produto '{row['produto_nome']}' tem baixo giro. Avaliar necessidade de estoque.")

