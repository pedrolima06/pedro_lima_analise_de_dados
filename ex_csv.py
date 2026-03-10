# LISTA DE EXERCÍCIOS – ANÁLISE DE DADOS COM PANDAS Dataset: Ranking
# Mundial de Universidades (notas.csv)

import pandas as pd
df = pd.read_csv('notas.csv')

# ============================================================
# EXPLORAÇÃO INICIAL (EDA BÁSICA)
# ============================================================

# Exercício 1 – Conhecendo o Dataset 
# 1. Quantas linhas e colunas existem?
# 2. Quais são os tipos de dados? 
# 3. Existe coluna com valores ausentes?
# 4. Qual é o período de anos disponível? 
# 5. Quantos países diferentes
# existem?
df.shape
df.dtypes
df.isnull().sum()
df['year'].unique()
df['country'].nunique()

# Exercício 2 – Estatísticas Gerais 
# 1. Média do score 
# 2. Maior score 
# 3.Menor score 
# 4. Média do score por ano 
# 5. Desvio padrão do score
df['score'].mean()
df['score'].max()
df['score'].min()
df.groupby('year')['score'].mean()
df['score'].std()

# ============================================================
# FILTROS E SELEÇÕES
# ============================================================

# Exercício 3 – Top Universidades 
# 1. Mostre as 10 melhores universidades do mundo (menor world_rank) 
# 2. Mostre as 5 melhores universidades do Brasil (se existirem) 
# 3. Mostre universidades com score maior que 90 
# 4. Mostre universidades dos EUA com score maior que 80
df.nsmallest(10, 'world_rank')[['institution', 'world_rank']]
df[df['country'] == 'Brazil'].nsmallest(5, 'world_rank')[['institution', 'world_rank']]
df[df['score'] > 90]['institution'].tolist()
df[(df['country'] == 'USA') & (df['score'] > 80)]['institution'].tolist()

# Exercício 4 – Seleção Avançada 
# 1. Mostre apenas as colunas: institution,
# country e score 
# 2. Mostre universidades entre rank 50 e 100 
# 3. Mostre universidades cujo país é “United Kingdom”
df[['institution', 'country', 'score']].head()
df[(df['world_rank'] >= 50) & (df['world_rank'] <= 100)][['institution', 'world_rank']].head()
df[df['country'] == 'United Kingdom']['institution'].head()

# ============================================================ PARTE 3 –
# MISSING VALUES
# ============================================================

# Exercício 5 – Valores Ausentes 
# 1. Quantos valores nulos existem na coluna broad_impact? 
# 2. Qual percentual do dataset é nulo? 
# 3. Remova linhas com broad_impact nulo 
# 4. Preencha valores nulos com a média 
# 5. Compare a média antes e depois do preenchimento
df['broad_impact'].isnull().sum()
(df.isnull().sum().sum() / (df.shape[0] * df.shape[1])) * 100
df_sem_nulos = df.dropna(subset=['broad_impact'])
media_broad = df['broad_impact'].mean()
df_preenchido = df.copy()
df_preenchido['broad_impact'] = df_preenchido['broad_impact'].fillna(media_broad)
(media_broad, df_preenchido['broad_impact'].mean())

# ============================================================ PARTE 4 –
# GROUPBY (ANÁLISE POR PAÍS E ANO)
# ============================================================

# Exercício 6 – Análise por País 
# 1. Média do score por país 
# 2. País com maior média de score 
# 3. Quantidade de universidades por país 
# 4. Top 10 países com mais universidades
df.groupby('country')['score'].mean().head()
df.groupby('country')['score'].mean().idxmax()
df.groupby('country')['institution'].nunique().head()
df.groupby('country')['institution'].nunique().nlargest(10)

# Exercício 7 – Análise por Ano 
# 1. Média do score por ano 
# 2. Qual ano teve maior média? 
# 3. Faça um gráfico da evolução do score médio ao longo do tempo
df.groupby('year')['score'].mean()
df.groupby('year')['score'].mean().idxmax()
df.groupby('year')['score'].mean().plot(kind='line', title='Evolução do Score Médio')