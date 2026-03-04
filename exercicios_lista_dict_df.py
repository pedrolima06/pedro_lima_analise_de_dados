"""
Aula - Exercicios de Pandas DataFrame
Como usar:
1) Leia o enunciado de cada bloco.
2) Complete o codigo onde estiver RESOLUCAO.
3) Rode o arquivo e valide os resultados.

Requisito:
- Instalar pandas: pip install pandas

Regra da aula:
- Pense no DataFrame como uma planilha.
- Resolva um exercicio por vez.
"""
# -------------------------------------------------
# BLOCO 1: criar DataFrame e inspecionar estrutura
# -------------------------------------------------
import pandas as pd 

dados_vendas = {
    "mes": ["Jan", "Jan", "Fev", "Fev", "Mar", "Mar"],
    "filial": ["Centro", "Norte", "Centro", "Norte", "Centro", "Norte"],
    "vendas": [12000, 9500, 13500, 10200, 14100, 11000],
    "clientes": [210, 180, 225, 190, 235, 205],
}

# Exercicio 1:
# a) Crie o DataFrame df_vendas usando dados_vendas
df_vendas = pd.DataFrame(dados_vendas)
# b) Mostre as 5 primeiras linhas
df_vendas.head()
# c) Mostre o formato (linhas, colunas)
df_vendas.shape
# d) Mostre os tipos de dados das colunas
df_vendas.dtypes


# -------------------------------------------------
# BLOCO 2: selecionar colunas e linhas
# -------------------------------------------------

# Exercicio 2:
# a) Mostre apenas as colunas "mes" e "vendas"
df_vendas[["mes", "vendas"]]

# b) Mostre somente a primeira linha
df_vendas.iloc[0]

# c) Mostre as linhas de indice 2 ate 4
df_vendas.iloc[2:5]


# -------------------------------------------------
# BLOCO 3: filtros com condicoes de negocio
# -------------------------------------------------

# Exercicio 3:
# a) Filtre vendas acima de 12000
df_vendas[df_vendas["vendas"] > 12000]

# b) Filtre apenas a filial "Centro"
df_vendas[df_vendas["filial"] == "Centro"]

# c) Filtre vendas acima de 11000 na filial "Norte"
df_vendas[(df_vendas["vendas"] > 11000) & 
          (df_vendas["filial"] == "Norte")]


# -------------------------------------------------
# BLOCO 4: novas colunas e metricas
# -------------------------------------------------

# Exercicio 4:
# a) Crie a coluna "ticket_medio" = vendas / clientes
df_vendas["ticket_medio"] = df_vendas["vendas"] / df_vendas["clientes"]

# b) Crie a coluna "meta_batida" com True para vendas >= 13000
df_vendas["meta_batida"] = df_vendas["vendas"] >= 13000

# c) Mostre apenas "filial", "mes", "ticket_medio", "meta_batida"
df_vendas[["filial", "mes", "ticket_medio", "meta_batida"]]


# -------------------------------------------------
# BLOCO 5: agregacao com groupby
# -------------------------------------------------

# Exercicio 5:
# a) Calcule total de vendas por filial
df_vendas.groupby("filial")["vendas"].sum()

# b) Calcule media de clientes por mes
df_vendas.groupby("mes")["clientes"].mean()

# c) Descubra a filial com maior total de vendas
df_vendas.groupby("filial")["vendas"].sum().idxmax()


# -------------------------------------------------
# BLOCO 6: ordenacao e ranking
# -------------------------------------------------

# Exercicio 6:
# a) Ordene df_vendas por "vendas" em ordem decrescente
df_ordenado = df_vendas.sort_values(by="vendas", ascending=False)

# b) Pegue os 3 maiores resultados de vendas
df_ordenado.head(3)

# c) Mostre um ranking com "filial", "mes", "vendas"
df_ordenado[["filial", "mes", "vendas"]]


# -------------------------------------------------
# BLOCO 7: desafio final de analise
# -------------------------------------------------

# Exercicio 7 (desafio):
# 1) Gere um resumo por filial com:
#    - total_vendas
#    - media_ticket_medio
#    - total_clientes
resumo = df_vendas.groupby("filial").agg(
    total_vendas=("vendas", "sum"),
    media_ticket_medio=("ticket_medio", "mean"),
    total_clientes=("clientes", "sum")
)

# 2) Ordene o resumo por total_vendas (desc)
resumo = resumo.sort_values(by="total_vendas", ascending=False)

# 3) Exiba qual filial teve melhor desempenho geral
resumo
resumo.index[0]


# ===========================================================
# PARTE 1 – Estrutura lista + dicionário
# ===========================================================

dados_list_dict = [{
    "Column A":[1, 2, 3],
    "Column B":[4, 5, 6],
    "Column C":[7, 8, 9]
}]

# -----------------------------------------------------------
# EXERCÍCIO 1 – Explorando a estrutura
# -----------------------------------------------------------

type(dados_list_dict)
type(dados_list_dict[0])
dados_list_dict[0]["Column A"]
dados_list_dict[0]["Column C"][1]


# -----------------------------------------------------------
# EXERCÍCIO 2 – Convertendo para DataFrame
# -----------------------------------------------------------

df1 = pd.DataFrame(dados_list_dict[0])

df1.shape
df1.dtypes
df1.sum()
df1.mean()


# -----------------------------------------------------------
# EXERCÍCIO 3 – Criando novas colunas
# -----------------------------------------------------------

df1["Total"] = df1.sum(axis=1)
df1["Media"] = df1[["Column A","Column B","Column C"]].mean(axis=1)
df1[df1["Total"] > 10]


# -----------------------------------------------------------
# EXERCÍCIO 4 – Conversões estruturais
# -----------------------------------------------------------

df1.to_dict(orient="records")
df1.to_dict(orient="list")


# -----------------------------------------------------------
# EXERCÍCIO 5 – Trabalhando com lista
# -----------------------------------------------------------

lista_a = df1["Column A"].to_list()
lista_a_x10 = [x * 10 for x in lista_a]
df1["Column A x10"] = lista_a_x10


# ===========================================================
# BASE DE DADOS
# ===========================================================

dados = [
    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-01", "valor": 5000},

    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 102, "descricao": "Produto B",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-01", "valor": 3000},

    {"id_pais": 1, "nome_pais": "Argentina", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-02", "valor": 4000},

    {"id_pais": 1, "nome_pais": "Argentina", "id_produto": 102, "descricao": "Produto B",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-02", "valor": 6000},

    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-03", "valor": 7000},
]

# ===========================================================
# PARTE 2 – CONVERSÃO PARA DATAFRAME
# ===========================================================

df = pd.DataFrame(dados)
df.shape
df.dtypes
df.head()

df["periodo"] = pd.to_datetime(df["periodo"])


# ===========================================================
# PARTE 3 – FILTROS
# ===========================================================

df[df["nome_pais"] == "Brasil"]
df[df["descricao"] == "Produto A"]
df[df["valor"] > 4000]
df[(df["nome_pais"] == "Brasil") & (df["descricao"] == "Produto A")]


# ===========================================================
# PARTE 4 – AGREGAÇÕES
# ===========================================================

df.groupby("nome_pais")["valor"].sum()
df.groupby("descricao")["valor"].sum()
df.groupby("nome_pais")["valor"].mean()
df.groupby("nome_pais")["valor"].count()

df.groupby(["nome_pais","descricao"])["valor"].agg(["sum","mean","count"])


# ===========================================================
# PARTE 5 – PIVOT TABLE
# ===========================================================

pivot_produto = df.pivot_table(
    index="periodo",
    columns="descricao",
    values="valor",
    aggfunc="sum"
)

pivot_produto

pivot_pais = df.pivot_table(
    index="periodo",
    columns="nome_pais",
    values="valor",
    aggfunc="sum"
)

pivot_pais


# ===========================================================
# PARTE 6 – FEATURE ENGINEERING
# ===========================================================

df["ano"] = df["periodo"].dt.year
df["mes"] = df["periodo"].dt.month
df["valor_mil"] = df["valor"] / 1000

df = df.sort_values(["descricao","periodo"])
df["crescimento_pct"] = df.groupby("descricao")["valor"].pct_change()


# ===========================================================
# PARTE 7 – QUALIDADE DE DADOS
# ===========================================================

df.isnull().sum()
(df["valor"] < 0).sum()
df.duplicated().sum()