"""
Aula - Exercicios de Dicionarios em Python
Como usar:
1) Leia o enunciado de cada bloco.
2) Complete o codigo onde estiver RESOLUCAO.
3) Rode o arquivo e valide os resultados com print.

Regra da aula:
- Foque no raciocinio: chave -> valor.
- Resolva um exercicio por vez.
"""

# -----------------------------------------
# BLOCO 1: criar e acessar chaves
# -----------------------------------------

faturamento_mensal = {"Jan": 12000, "Fev": 15000, "Mar": 9000}

# Exercicio 1:
# a) Mostre o faturamento de Fev
# b) Mostre todas as chaves
# c) Mostre todos os valores

faturamento_mensal['Fev']
list(faturamento_mensal.keys())
list(faturamento_mensal.values())


# Exercicio 2:
# O valor de Mar estava errado. Atualize para 9800.
# Depois, adicione Abr com valor 13200.

faturamento_mensal["Mar"] = 9800
faturamento_mensal["Abr"] = 13200
faturamento_mensal


# -----------------------------------------
# BLOCO 2: metodos e seguranca
# -----------------------------------------

estoque = {"caneta": 120, "caderno": 80, "lapis": 200}

# Exercicio 3:
# a) Verifique se a chave "borracha" existe
# b) Se nao existir, retorne 0 usando get
# c) Mostre o estoque de "lapis" com get

'borracha' in estoque
estoque.get('borracha', 0)
estoque.get('lapis')


# Exercicio 4:
# Remova "caneta" do estoque e mostre o dicionario final.
# Dica: use pop.

estoque.pop("caneta", None)
estoque


# -----------------------------------------
# BLOCO 3: percorrer e agregar
# -----------------------------------------

vendas_por_regiao = {
    "Norte": 18000,
    "Nordeste": 22000,
    "Centro-Oeste": 17000,
    "Sudeste": 30000,
    "Sul": 21000,
}

# Exercicio 5:
# a) Calcule o total vendido no pais
# b) Encontre a regiao com maior valor de vendas
# c) Encontre a regiao com menor valor de vendas

sum(vendas_por_regiao.values())
max(vendas_por_regiao, key=vendas_por_regiao.get)
min(vendas_por_regiao, key=vendas_por_regiao.get)


# Exercicio 6:
# Percorra o dicionario e mostre somente regioes com vendas acima de 20000.

[regiao for regiao, valor in vendas_por_regiao.items() if valor > 20000]


# -------------------------------------------------
# BLOCO 4: dicionario como acumulador
# -------------------------------------------------

vendas_produtos = [
    ("Notebook", 1),
    ("Mouse", 2),
    ("Notebook", 1),
    ("Teclado", 1),
    ("Mouse", 1),
]

# Exercicio 7:
# Construa um dicionario de contagem no formato:
# {"Notebook": 2, "Mouse": 3, "Teclado": 1}
#
# Dica:
# - Se a chave nao existir, comeca em 0
# - Depois soma a quantidade

contagem = {}
for p, qtd in vendas_produtos:
    contagem[p] = contagem.get(p, 0) + qtd
contagem


# ---------------------------------------------------
# BLOCO 5: desafio final de negocio
# ---------------------------------------------------

# Lista de vendas (registro por transacao)
transacoes = [
    {"mes": "Jan", "valor": 1200},
    {"mes": "Jan", "valor": 800},
    {"mes": "Fev", "valor": 1500},
    {"mes": "Fev", "valor": 700},
    {"mes": "Mar", "valor": 1300},
]

# Exercicio 8 (desafio):
# 1) Crie um dicionario total_por_mes e acumule os valores
# 2) Mostre o mes com maior faturamento
# 3) Mostre o total geral do trimestre
# 4) Mostre a media mensal (total/numero de meses no dicionario)

total_por_mes = {}
for t in transacoes:
    total_por_mes[t["mes"]] = total_por_mes.get(t["mes"], 0) + t["valor"]

total_por_mes
max(total_por_mes, key=total_por_mes.get)
sum(total_por_mes.values())
sum(total_por_mes.values()) / len(total_por_mes)


# ---------------------
# CHECKLIST DE REVISAO
# ---------------------
#
# [ ] Sei criar e atualizar dicionarios
# [ ] Sei acessar chaves com seguranca (get, in)
# [ ] Sei percorrer com keys, values, items
# [ ] Sei usar dicionario para acumulacao
# [ ] Sei aplicar dicionarios em cenarios de negocio