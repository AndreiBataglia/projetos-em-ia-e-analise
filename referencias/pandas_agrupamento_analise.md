🐼 Guia de Agrupamentos e Análises com Pandas
🔹 Agrupamento por múltiplas colunas
Agrupa os dados por mais de uma variável para obter estatísticas específicas por combinação:

df.groupby(["variavel1", "variavel2", "variavel3"])["coluna_interesse"].mean()

🔹 Tornar o resultado legível com .reset_index()
Converte o índice hierárquico em colunas normais:

df.groupby(["categoria", "grupo"])["resultado"].mean().reset_index()

🔹 Pivotagem com .pivot_table()
Cria uma tabela dinâmica para cruzamento de informações:

df.pivot_table(values="valor", index="grupo", columns="categoria", aggfunc="mean")

🔹 Múltiplas estatísticas com .agg()
Permite aplicar diferentes funções a diferentes colunas:

df.groupby("grupo").agg({"coluna1": "mean", "coluna2": "sum"})

🔹 Visualização com Seaborn
Gráfico de barras com múltiplas categorias:
sns.barplot(data=df, x="categoria", y="resultado", hue="grupo")

Boxplot por categoria:
sns.boxplot(data=df, x="categoria", y="valor")

Dispersão com coloração por grupo:
sns.scatterplot(data=df, x="variavel_x", y="variavel_y", hue="grupo")

🔹 Sugestões de agrupamentos úteis
Agrupamento	Aplicação
["produto", "regiao"]	Comparação regional de vendas ou produção
["ano", "mes"]	Análise temporal ou sazonalidade
["cliente", "categoria"]	Segmentação de comportamento
["item", "clima"]	Avaliação ambiental aplicada
🔹 Dicas finais
Ordenar resultados:
df.sort_values("coluna", ascending=False)

Visualização em notebook com gradiente:
df.style.background_gradient(cmap="Blues")