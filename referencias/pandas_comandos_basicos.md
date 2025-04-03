
# 🐼 Lista de Comandos e Métodos Essenciais do Pandas

## 🔹 Leitura e Escrita de Arquivos
pd.read_csv("arquivo.csv")  
pd.read_excel("arquivo.xlsx")  
df.to_csv("saida.csv", index=False)  
df.to_excel("saida.xlsx", index=False)

## 🔹 Exploração Inicial
df.head()           # Primeiras linhas  
df.tail()           # Últimas linhas  
df.info()           # Estrutura do DataFrame  
df.describe()       # Estatísticas descritivas  
df.shape            # (linhas, colunas)  
df.columns          # Lista de colunas  
df.dtypes           # Tipos de dados por coluna

## 🔹 Seleção de Dados
df["coluna"]                      # Seleção de coluna  
df[["col1", "col2"]]              # Seleção múltipla  
df.iloc[0]                        # Linha por índice  
df.loc[0]                         # Linha por rótulo  
df.iloc[0, 1]                     # Célula específica  
df[df["coluna"] > 100]           # Filtro por condição  
df.query("coluna > 100")         # Filtro com query

## 🔹 Manipulação de Colunas
df["nova"] = df["col1"] + df["col2"]          # Nova coluna  
df.drop("coluna", axis=1, inplace=True)       # Remover coluna  
df.rename(columns={"antigo": "novo"}, inplace=True)  # Renomear

## 🔹 Tratamento de Dados
df.isnull().sum()                # Verificar nulos  
df.dropna()                      # Remover nulos  
df = df.dropna(subset=["coluna"])

print(f"Nº de linhas após limpeza: {df.shape[0]}") #Verficar quantidade de linhas removidas

df.fillna(valor)                 # Preencher nulos  
df.duplicated().sum()            # Verificar duplicatas  
df.drop_duplicates(inplace=True) # Remover duplicatas  
df["coluna"] = df["coluna"].astype(int)       # Conversão de tipo

## 🔹 Agrupamento e Estatísticas
df.groupby("coluna")["valor"].mean()  
df.groupby("coluna").agg(["mean", "sum", "std"])  

df.groupby("id_equipamento")["horas_uso"].agg(["mean", "std", "min"])
df.groupby("id_equipamento").agg({
    "horas_uso": "mean",
    "erro_sensor": "sum"  # Total de erros por equipamento
})

df["coluna"].value_counts()      # Contagem de valores únicos  
df["coluna"].nunique()           # Quantidade de valores únicos

## 🔹 Ordenação
df.sort_values("coluna")  
df.sort_values("coluna", ascending=False)

## 🔹 Criação de Faixas/Categorias
pd.cut(df["coluna"], bins=[0,10,20], labels=["baixo", "alto"])  
pd.qcut(df["coluna"], q=4)

## 🔹 Junções (merge)
pd.merge(df1, df2, on="id")  
df1.join(df2)

## 🔹 Exportação
df.to_csv("saida.csv", index=False)
