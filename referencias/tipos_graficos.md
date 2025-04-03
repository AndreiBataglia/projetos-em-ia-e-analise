
# 📊 Tipos de Gráficos e Quando Utilizá-los

Este guia resume os principais tipos de gráficos usados em análise de dados com `matplotlib` e `seaborn`, explicando **quando** e **por que** usá-los.

---

## 📈 1. **Line Plot (Gráfico de Linha)**

**Uso:** Mostrar tendências ao longo do tempo.

```python
plt.plot(df["data"], df["valor"])
```

✅ Ideal para: séries temporais, variações por dia, mês, etc.

---

## 📊 2. **Bar Plot (Gráfico de Barras)**

**Uso:** Comparar valores entre categorias.

```python
sns.barplot(x="categoria", y="valor", data=df)
```

✅ Ideal para: comparar turnos, máquinas, faixas de idade, etc.

---

## 📊 3. **Count Plot (Contagem por Categoria)**

**Uso:** Mostrar quantas vezes cada valor aparece.

```python
sns.countplot(x="coluna", data=df)
```

✅ Ideal para: ver frequência de rótulos, contagem de classes.

---

## 📊 4. **Histogram (Histograma)**

**Uso:** Distribuição de uma variável numérica.

```python
sns.histplot(df["valor"], bins=20)
```

✅ Ideal para: visualizar dispersão, concentração de valores.

---

## 📊 5. **Box Plot (Diagrama de Caixa)**

**Uso:** Comparar distribuições, detectar outliers.

```python
sns.boxplot(x="categoria", y="valor", data=df)
```

✅ Ideal para: variabilidade por turno, máquina ou grupo.

---

## 📊 6. **Violin Plot**

**Uso:** Visualizar densidade da distribuição + estatísticas.

```python
sns.violinplot(x="grupo", y="valor", data=df)
```

✅ Ideal para: análises comparativas detalhadas.

---

## 📊 7. **Scatter Plot (Dispersão)**

**Uso:** Relacionar duas variáveis numéricas.

```python
sns.scatterplot(x="x", y="y", data=df, hue="grupo")
```

✅ Ideal para: correlação, tendências entre variáveis.

---

## 📊 8. **Heatmap (Mapa de Calor)**

**Uso:** Visualizar correlação entre variáveis ou matrizes.

```python
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
```

✅ Ideal para: entender relações entre variáveis numéricas.

---

## 📊 9. **Pie Chart (Gráfico de Pizza)**

**Uso:** Proporção entre categorias (usado com cautela).

```python
df["categoria"].value_counts().plot.pie(autopct="%1.1f%%")
```

⚠️ Use com poucas categorias (3–5) para não dificultar a leitura.

---

## 🎯 Escolhendo o gráfico certo

| Objetivo | Gráfico Ideal |
|---------|----------------|
| Evolução ao longo do tempo | Line Plot |
| Comparar categorias | Bar Plot |
| Ver frequência | Count Plot |
| Visualizar distribuição | Histogram |
| Comparar grupos + detectar outliers | Box Plot |
| Ver relação entre duas variáveis | Scatter Plot |
| Ver correlações | Heatmap |
| Proporções simples | Pie Chart |

---

## 📚 Recursos úteis

- [Seaborn Examples](https://seaborn.pydata.org/examples/index.html)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)

