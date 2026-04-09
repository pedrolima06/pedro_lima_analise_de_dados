"""
Aula - Exercicios de Filtros Regex com Pandas DataFrame
Como usar:
1) Leia o enunciado de cada bloco.
2) Complete o codigo onde estiver RESOLUCAO.
3) Rode o arquivo e valide os resultados com print.

Requisito:
- Instalar pandas: pip install pandas

Regra da aula:
- Regex ajuda a filtrar texto com padroes.
- Resolva um exercicio por vez.
"""

import pandas as pd


# -------------------------------------------------
# BLOCO 1: base de dados para praticar regex
# -------------------------------------------------

dados_clientes = {
    "cliente": [
        "Ana Souza",
        "Bruno Lima",
        "Carla Mendes",
        "Daniel Rocha",
        "Empresa XPTO Ltda",
        "Mercado Bom Preco",
    ],
    "email": [
        "ana.souza@gmail.com",
        "bruno_lima@empresa.com.br",
        "carla.mendes@yahoo.com",
        "daniel@outlook.com",
        "contato@xpto.com.br",
        "vendas@bompreco.com.br",
    ],
    "cidade": ["Sao Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Sao Paulo", "Curitiba"],
    "codigo_cliente": ["CLI-001", "CLI-002", "VIP-101", "CLI-003", "EMP-501", "VIP-102"],
}

# Exercicio 1:
# a) Crie o DataFrame df_clientes
# b) Mostre as primeiras linhas

df_clientes = pd.DataFrame(dados_clientes)
df_clientes.head()


# -------------------------------------------------
# BLOCO 2: filtros basicos com str.contains
# -------------------------------------------------

# Exercicio 2:
# Filtre os registros onde:
# a) email termina com ".com.br"
# b) cliente contem a palavra "Mercado"
# c) codigo_cliente comeca com "VIP"
#
# Dica:
# Use str.contains com padroes regex:
# - r"\.com\.br$"
# - r"Mercado"
# - r"^VIP"

df_clientes[df_clientes['email'].str.contains(r"\.com\.br$", regex=True)]
df_clientes[df_clientes['cliente'].str.contains(r"Mercado", regex=True)]
df_clientes[df_clientes['codigo_cliente'].str.contains(r"^VIP", regex=True)]


# -------------------------------------------------
# BLOCO 3: classes de caracteres e quantificadores
# -------------------------------------------------

# Exercicio 3:
# Filtre os clientes cujo codigo esteja no formato:
# 3 letras maiusculas + "-" + 3 digitos
# Exemplo valido: CLI-001
#
# Dica de regex:
# r"^[A-Z]{3}-\d{3}$"

df_clientes[df_clientes['codigo_cliente'].str.contains(r"^[A-Z]{3}-\d{3}$", regex=True)]


# -------------------------------------------------
# BLOCO 4: alternancia e grupos
# -------------------------------------------------

# Exercicio 4:
# Encontre emails que sejam de:
# - gmail.com OU outlook.com
#
# Dica de regex:
# r"@(gmail|outlook)\.com$"

df_clientes[df_clientes['email'].str.contains(r"@(gmail|outlook)\.com$", regex=True)]


# -------------------------------------------------
# BLOCO 5: ignorar maiusculas/minusculas e nulos
# -------------------------------------------------

# Inclui valores com caixa diferente e um valor ausente.
df_leads = pd.DataFrame(
    {
        "origem": ["Instagram", "instagram", "LinkedIn", "EMAIL", None, "Google Ads"],
        "campanha": ["Promo Verao", "promo verao", "B2B_Q1", "BLACK_FRIDAY", "Teste", "Leads_2026"],
    }
)

# Exercicio 5:
# a) Filtre origem contendo "instagram" sem diferenciar maiusculas/minusculas
# b) Filtre campanhas que tenham apenas letras, espacos e underscore
# c) Garanta que valores nulos nao quebrem o filtro
#
# Dicas:
# - case=False
# - na=False
# - regex sugerida para (b): r"^[A-Za-z_ ]+$"

df_leads[df_leads['origem'].str.contains(r"instagram", case=False, na=False, regex=True)]
df_leads[df_leads['campanha'].str.contains(r"^[A-Za-z_ ]+$", na=False, regex=True)]


# -------------------------------------------------
# BLOCO 6: desafio final de negocio
# -------------------------------------------------

# Exercicio 6 (desafio):
# Usando df_clientes:
# 1) Crie um filtro para clientes pessoa juridica
#    (nomes contendo "Ltda" ou "Mercado")
# 2) Crie um filtro para clientes VIP (codigo iniciando com VIP)
# 3) Crie um filtro para emails corporativos ".com.br"
# 4) Monte um DataFrame final apenas com registros que atendam
#    pelo menos 2 dos 3 criterios acima

cond1 = df_clientes['cliente'].str.contains(r"Ltda|Mercado", case=False, regex=True)
cond2 = df_clientes['codigo_cliente'].str.contains(r"^VIP", regex=True)
cond3 = df_clientes['email'].str.contains(r"\.com\.br$", regex=True)

df_clientes['criterios'] = cond1.astype(int) + cond2.astype(int) + cond3.astype(int)
df_desafio = df_clientes[df_clientes['criterios'] >= 2].drop(columns=['criterios'])
df_desafio


# ---------------------
# CHECKLIST DE REVISAO
# ---------------------
#
# [ ] Sei usar str.contains com regex
# [ ] Sei usar inicio (^) e fim ($) de string
# [ ] Sei usar grupos e alternancia (|)
# [ ] Sei usar classes e quantificadores ({}, \d)
# [ ] Sei usar case=False e na=False
# [ ] Sei aplicar filtros regex em cenarios de negocio