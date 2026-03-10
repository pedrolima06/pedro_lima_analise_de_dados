"""
Aula - Variaveis e Tipos Basicos em Python
Objetivo:
- Entender o que e uma variavel
- Conhecer tipos basicos: str, int, float, bool
- Aplicar em cenarios simples de negocio
"""

# ------------------------------------------------
# BLOCO 1: o que e variavel na pratica
# ------------------------------------------------
#
# Variavel = "caixa com nome" para guardar um valor.
# Exemplo em negocio:
# - nome_empresa guarda texto
# - funcionarios guarda numero inteiro
# - taxa_juros guarda numero com casas decimais

nome_empresa = "Loja Centro"
funcionarios = 12
taxa_juros = 1.75
empresa_ativa = True

nome_empresa, funcionarios, taxa_juros, empresa_ativa


# ------------------------------------------------
# BLOCO 2: tipos basicos e type()
# ------------------------------------------------

type(nome_empresa)
type(funcionarios)
type(taxa_juros)
type(empresa_ativa)

# Exercicio 1:
# Crie as variaveis abaixo com os tipos corretos:
# a) produto = "Notebook Pro"
# b) estoque = 45
# c) preco = 3499.90
# d) em_promocao = False

produto = "Notebook Pro"
estoque = 45
preco = 3499.90
em_promocao = False
(type(produto), type(estoque), type(preco), type(em_promocao))


# ------------------------------------------------
# BLOCO 3: entrada, conversao e cuidado
# ------------------------------------------------

# Em Python, dados podem vir como texto (str).
# Para calcular, as vezes precisamos converter.

quantidade_str = "10"
preco_str = "25.5"

quantidade = int(quantidade_str)
preco_unitario = float(preco_str)
total = quantidade * preco_unitario

total

# Exercicio 2:
# Converta os valores e calcule:
# faturamento_str = "15890.75"
# custo_str = "9230.10"
# lucro = faturamento - custo

faturamento_str = "15890.75"
custo_str = "9230.10"

faturamento = float(faturamento_str)
custo = float(custo_str)
lucro = faturamento - custo
lucro


# ------------------------------------------------
# BLOCO 4: operacoes com tipos basicos
# ------------------------------------------------

vendas_jan = 12000
vendas_fev = 14500
meta_batida = vendas_fev > 13000

vendas_jan + vendas_fev
(vendas_jan + vendas_fev) / 2
meta_batida

# Exercicio 3:
# Crie um mini painel com variaveis:
# - clientes_ativos (int)
# - ticket_medio (float)
# - nome_gerente (str)
# - equipe_completa (bool)
#
# Depois mostre uma frase com f-string:
# "Gerente X acompanha Y clientes com ticket medio de Z."

clientes_ativos = 150
ticket_medio = 450.50
nome_gerente = "Carlos"
equipe_completa = True

f"Gerente {nome_gerente} acompanha {clientes_ativos} clientes com ticket medio de {ticket_medio:.2f}."


# ------------------------------------------------
# BLOCO 5: pratica focada em f-string
# ------------------------------------------------

# Exercicio 4:
# Monte um resumo executivo usando f-string.
# Use os dados abaixo e exiba:
# "A loja X faturou R$ Y no mes, com crescimento de Z% e status W."
#
# Regras:
# - faturamento com 2 casas decimais
# - crescimento com 1 casa decimal

loja = "Loja Centro"
faturamento_mes = 27890.5
crescimento_percentual = 6.37
status_meta = True

f"A {loja} faturou R$ {faturamento_mes:.2f} no mes, com crescimento de {crescimento_percentual:.1f}% e status {status_meta}."


# ------------------------------------------------
# BLOCO 6: desafio final integrando tudo
# ------------------------------------------------

# Cenario:
# Uma loja quer calcular margem de lucro e status da meta.

receita = 25000.0
custos = 17800.0
meta_receita = 24000.0

# Exercicio 5 (desafio):
# 1) Crie variavel lucro = receita - custos
# 2) Crie variavel margem = (lucro / receita) * 100
# 3) Crie variavel bateu_meta (bool)
# 4) Mostre resultados com 2 casas decimais
#
# Dica:
# print(f"Margem: {margem:.2f}%")

lucro = receita - custos
margem = (lucro / receita) * 100
bateu_meta = receita >= meta_receita

(f"Lucro: R$ {lucro:.2f}", f"Margem: {margem:.2f}%", f"Bateu Meta: {bateu_meta}")


# ---------------------
# CHECKLIST DE REVISAO
# ---------------------
#
# [ ] Entendo o que e variavel
# [ ] Sei identificar str, int, float, bool
# [ ] Sei usar type() para conferir tipos
# [ ] Sei converter texto para numero com int/float
# [ ] Sei montar calculos simples de negocio