
# 📊 Estatísticas com Pandas: Guia de Funções e Parâmetros

Este documento reúne as principais funções estatísticas e métodos agregadores utilizados com o Pandas. Ideal para análise de dados e geração de insights a partir de DataFrames.

---

## 🧠 Funções Estatísticas Individuais

| Função | Descrição | Exemplo |
|--------|-----------|---------|
| `mean()` | Média aritmética | `df["coluna"].mean()` |
| `median()` | Mediana (valor central) | `df["coluna"].median()` |
| `mode()` | Moda (valor mais frequente) | `df["coluna"].mode()` |
| `std()` | Desvio padrão | `df["coluna"].std()` |
| `var()` | Variância | `df["coluna"].var()` |
| `min()` | Valor mínimo | `df["coluna"].min()` |
| `max()` | Valor máximo | `df["coluna"].max()` |
| `sum()` | Soma total | `df["coluna"].sum()` |
| `count()` | Contagem (exclui NaN) | `df["coluna"].count()` |
| `nunique()` | Nº de valores únicos | `df["coluna"].nunique()` |
| `value_counts()` | Frequência de cada valor | `df["coluna"].value_counts()` |

---

## 🧩 `agg()` — Agregações múltiplas

Permite aplicar várias funções de uma vez, especialmente útil com `groupby`.

```python
df.groupby("categoria")["valor"].agg(["mean", "std", "min", "max"])
```

Exemplo prático:
```python
df.groupby("turno")["pecas_produzidas"].agg(["mean", "std"])
```

---

## 📊 `describe()` — Estatísticas Resumidas

```python
df["coluna"].describe()
```

| Estatística | Significado |
|-------------|-------------|
| count | Nº de registros válidos |
| mean | Média |
| std | Desvio padrão |
| min | Mínimo |
| 25% | Primeiro quartil |
| 50% | Mediana |
| 75% | Terceiro quartil |
| max | Máximo |

---

## 🧮 Exemplo Completo com GroupBy

```python
df.groupby("maquina_id")["eficiencia_%"].agg(
    media="mean",
    desvio="std",
    minimo="min",
    maximo="max"
)
```

Resultado:

| maquina_id | media | desvio | minimo | maximo |
|------------|-------|--------|--------|--------|
| M1         | 92.3  | 3.2    | 85.4   | 97.6   |
| M2         | 94.1  | 2.7    | 89.1   | 99.3   |

---

## 🧠 Dicas Importantes

- Use `agg()` para aplicar múltiplas funções com nomes personalizados.
- Use `reset_index()` se quiser transformar os índices em colunas.
- Combine com `cut()` ou `qcut()` para análises por faixa.

---

## 📌 Recursos Complementares

- [Documentação Oficial do Pandas](https://pandas.pydata.org/docs/)
- [Visualização com Seaborn](https://seaborn.pydata.org/)
- [Análise Exploratória de Dados](https://realpython.com/pandas-python-explore-dataset/)

---

Pronto para aplicar essas técnicas nas suas análises? Use este guia como referência para interpretar e comunicar dados com clareza!
