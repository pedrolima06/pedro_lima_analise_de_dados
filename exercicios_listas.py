"""
Aula - Exercicios de Listas em Python
Como usar:
1) Leia o enunciado de cada bloco.
2) Complete o codigo onde estiver RESOLUCAO.
3) Rode o arquivo e compare com o resultado esperado (quando informado).

Regra da aula:
- Nao use IA para gerar resposta final.
- Resolva passo a passo e valide com print.
"""

# ------------------------------
# BLOCO 1: fundamentos
# ------------------------------

vendas_semana = [1200, 980, 1430, 1100, 1600]

# Exercicio 1:
# Mostre:
# a) numero de dias vendidos
# b) total vendido na semana
# c) maior e menor venda diaria

# RESOLUCAO: complete aqui
print("Dias vendidos:", len(vendas_semana))
print("Total vendido:", sum(vendas_semana))
print("Maior venda:", max(vendas_semana), "| Menor venda:", min(vendas_semana))


# Exercicio 2:
# Acesse e mostre:
# a) primeira venda
# b) ultima venda
# c) vendas do meio (sem primeira e ultima)

# RESOLUCAO: complete aqui
print("\nPrimeira venda:", vendas_semana[0])
print("Última venda:", vendas_semana[-1])
print("Vendas do meio:", vendas_semana[1:-1])


# -----------------------------------
# BLOCO 2: alterar e limpar
# -----------------------------------

custos_marketing = [350, 420, 390, 410]

# Exercicio 3:
# a) Adicione um novo custo de 460 no final
# b) Insira 300 no inicio da lista
# c) Remova o valor 390
# d) Mostre a lista final

# RESOLUCAO: complete aqui
custos_marketing.append(460)
custos_marketing.insert(0, 300)
custos_marketing.remove(390)
print("\nLista final marketing:", custos_marketing)


# Exercicio 4:
# A lista abaixo tem um lancamento duplicado por erro.
# Remova somente uma ocorrencia de 1200.

vendas_com_erro = [900, 1200, 1500, 1200, 1800]
# RESOLUCAO: complete aqui
vendas_com_erro.remove(1200)
print("Vendas corrigidas:", vendas_com_erro)


# -----------------------------------------
# BLOCO 3: ordenacao e filtragem
# -----------------------------------------

ticket_medio_filiais = [85, 120, 73, 150, 99, 135]

# Exercicio 5:
# a) Crie uma nova lista em ordem crescente (sem perder a original)
# b) Crie outra em ordem decrescente
# c) Mostre as tres listas

# RESOLUCAO: complete aqui
lista_crescente = sorted(ticket_medio_filiais)
lista_decrescente = sorted(ticket_medio_filiais, reverse=True)

print("\nLista original:", ticket_medio_filiais)
print("Ordem crescente:", lista_crescente)
print("Ordem decrescente:", lista_decrescente)


# Exercicio 6:
# Gere uma lista apenas com tickets acima de 100.
# Dica: use for + if, ou list comprehension.

# RESOLUCAO: complete aqui
acima_100 = [t for t in ticket_medio_filiais if t > 100]
print("Tickets > 100:", acima_100)


# ---------------------------------------
# BLOCO 4: agregacao e tomada
# ---------------------------------------

faturamento_diario = [2100, 1800, 2500, 1950, 2300]

# Exercicio 7:
# a) Calcule a media de faturamento diario
# b) Conte quantos dias ficaram acima da media
# c) Mostre os valores desses dias

# RESOLUCAO: complete aqui
media = sum(faturamento_diario) / len(faturamento_diario)
acima_media = [f for f in faturamento_diario if f > media]

print(f"\nMédia: {media:.2f}")
print("Quantidade de dias > média:", len(acima_media))
print("Dias > média:", acima_media)


# ---------------------------------------
# BLOCO 5: desafio final guiado
# ---------------------------------------

# Cenário:
# Sua empresa registrou vendas por vendedor na semana.
vendas_vendedor = [450, 520, 610, 480, 700, 530, 620]

# Exercicio 8 (desafio):
# 1) Calcule total e media semanal
# 2) Crie uma lista com vendas acima de 550
# 3) Mostre os 3 maiores valores de venda
# 4) Informe quantos dias ficaram abaixo de 500

# RESOLUCAO: complete aqui
print(f"\nTotal semanal: {sum(vendas_vendedor)} | Média: {sum(vendas_vendedor)/len(vendas_vendedor):.2f}")
print("Vendas > 550:", [v for v in vendas_vendedor if v > 550])
print("Top 3 vendas:", sorted(vendas_vendedor, reverse=True)[:3])
print("Dias < 500:", len([v for v in vendas_vendedor if v < 500]))


# ---------------------
# CHECKLIST DE REVISAO
# ---------------------
#
# [ ] Sei criar listas e acessar por indice
# [ ] Sei usar len, sum, min, max
# [ ] Sei adicionar/remover itens
# [ ] Sei ordenar sem perder dados originais
# [ ] Sei filtrar listas com condicoes
# [ ] Sei aplicar listas em cenarios de negocio