import pandas as pd
import numpy as np

# Geração do dataset simulado
np.random.seed(42)
n = 100

df = pd.DataFrame({
    "data": pd.date_range(start="2023-01-01", periods=n, freq="D"),
    "turno": np.random.choice(["Manhã", "Tarde", "Noite"], size=n),
    "maquina_id": np.random.choice(["M1", "M2", "M3"], size=n),
    "pecas_produzidas": np.random.randint(200, 500, size=n),
    "pecas_defeituosas": np.random.randint(0, 50, size=n),
    "temperatura": np.round(np.random.normal(loc=75, scale=5, size=n), 1),
    "umidade": np.round(np.random.normal(loc=45, scale=10, size=n), 1)
})

# Cálculo da eficiência
df["eficiencia_%"] = (
    (df["pecas_produzidas"] - df["pecas_defeituosas"]) / df["pecas_produzidas"]
) * 100

# Salvar em CSV
df.to_csv("dados_producao.csv", index=False)

print("✅ Dataset 'dados_producao.csv' criado com sucesso!")
