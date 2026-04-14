# O dataset NCR Ride Bookings contém registros de corridas urbanas realizadas em regiões da National Capital Region (NCR), que abrange Delhi, Gurgaon, Noida, Ghaziabad, Faridabad e áreas próximas.
# Utilize os arquivos : ncr_ride_bookings.csv para resolver as questoes.
# Principais informaçoes no dataset:
# Date → Data da corrida
# Time → Horário da corrida
# Booking ID → Identificador da corrida
# Booking Status → Status da corrida
# Customer ID → Identificador do cliente
# Vehicle Type → Tipo de veículo
# Pickup Location → Local de embarque
# Drop Location → Local de desembarque
# Booking Value → Valor da corrida
# Ride Distance → Distância percorrida
# Driver Ratings → Avaliação do motorista
# Customer Rating → Avaliação do cliente
# Payment Method → Método de pagamento

import pandas as pd
import requests

df = pd.read_csv("ncr_ride_bookings.csv")


# Questões:
# (0,5) 1 - Quantas corridas estão com Status da Corrida como Completada ("Completed") no dataset? 
completas = df[df["Booking Status"] == "Completed"].shape[0]

# (0,5) 2 - Qual a proporção em relação ao total de corridas?
proporcao = completas / df.shape[0]

# (0,5) 3 - Calcule a média da Distância ("Ride Distance") percorrida por cada Tipo de veículo.
df.groupby("Vehicle Type")["Ride Distance"].mean()

# (0,5) 4 - Qual o Metodo de Pagamento ("Payment Method") mais utilizado pelas bicicletas ("Bike") ?
df[df["Vehicle Type"] == "Bike"]["Payment Method"].mode()[0]
        
# (0,5) 5 - Qual o valor total arrecadado ("Booking Value") apenas das corridas Completed?
df[df["Booking Status"] == "Completed"]["Booking Value"].sum()

# (0,5) 6 - E qual o ticket médio ("Booking Value")dessas corridas Completed?
df[df["Booking Status"] == "Completed"]["Booking Value"].mean()

# (1,5) 7 - O IPEA disponibiliza uma API pública com diversas séries econômicas. 
# Para encontrar a série de interesse, é necessário primeiro acessar o endpoint de metadados.
# Acesse o endpoint de metadados: "http://www.ipeadata.gov.br/api/odata4/Metadados";
# Transforme em um DataFrame;
# Filtre para encontrar as séries da Fipe relacionadas a venda de imoveis (“vendas - Brasil”).
# Dica: 
# Utilize a coluna FNTSIGLA para encontrar a serie da Fipe;
# Utilize a coluna SERNOME para encontrar as vendas de imoveis no Brasil;
url = "http://www.ipeadata.gov.br/api/odata4/Metadados"
meta = requests.get(url).json()
df = pd.DataFrame(meta["value"])
fipe_vendas = df[
    (df["FNTSIGLA"].str.contains("FIPE", case=False, na=False)) &
    (df["SERNOME"].str.contains("vendas", case=False, na=False)) &
    (df["SERNOME"].str.contains("Brasil", case=False, na=False))
]

# (1,5) 8 -  Descubra qual é o código da série correspondente (coluna: SERCODIGO).
# CODIGO_ENCONTRADO=''
# Usando o código encontrado, acesse a API de valores: f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"
# Construa um DataFrame através da chave 'value' do retorno da api
# Selecione apenas as colunas datas (VALDATA) e os valores (VALVALOR).
# Exiba a Data e o Valor que teve o valor maximo de vendas.
CODIGO = fipe_vendas["SERCODIGO"].iloc[0]
url = f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO}')"
valores = requests.get(url).json()
df = pd.DataFrame(valores["value"])[["VALDATA","VALVALOR"]]
max_venda = df.loc[df["VALVALOR"].idxmax()]

# (1,5) 9 - Descubra quanto rendeu a VALE no ano de 2025
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# params = {"ticker": "VALE3", "data_ini": "2001-01-01", "data_fim": "2026-12-31"}
# response = requests.get(
#     f"{base_url}/preco/corrigido",
#     headers={"Authorization": f"Bearer {token}"},
#     params=params,
# )
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2NTEyNTM5LCJpYXQiOjE3NzM5MjA1MzksImp0aSI6ImIwNTU4OTQwMzgzYTRlMDlhNmFjMzIyYTk0OGYwM2UxIiwidXNlcl9pZCI6Ijk4In0.vpr-Le2G9XHbJsykBktBJ6FI6P1qq5L0a31DLQMBoV0"
params = {"ticker": "VALE3", "data_ini": "2001-01-01", "data_fim": "2026-12-31"}
response = requests.get(
    f"{base_url}/preco/corrigido",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)
df = pd.DataFrame(response.json())
df[df["data"].str.contains("2025")]["preco"].sum()

# (1,5) 10 - Você tem acesso à API do Laboratório de Finanças, que fornece dados do Planilhão em formato JSON. 
# Selecione a empresa do setor de "tecnologia" que apresenta o maior ROE (Return on Equity) na data base 2024-04-01.
# Exiba APENAS AS COLUNAS "ticker", "setor" e o "roe"
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# response = requests.get(
#     f"{base_url}/bolsa/planilhao",
#     headers={"Authorization": f"Bearer {token}"},
#     params={"data_base": "2026-04-01"},
# )
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2NTEyNTM5LCJpYXQiOjE3NzM5MjA1MzksImp0aSI6ImIwNTU4OTQwMzgzYTRlMDlhNmFjMzIyYTk0OGYwM2UxIiwidXNlcl9pZCI6Ijk4In0.vpr-Le2G9XHbJsykBktBJ6FI6P1qq5L0a31DLQMBoV0"
response = requests.get(
     f"{base_url}/bolsa/planilhao",
     headers={"Authorization": f"Bearer {token}"},
     params={"data_base": "2026-04-01"}, 
)
pd.DataFrame(response.json())
tecnologia = df[df["setor"]=="tecnologia"]
maior_roe = tecnologia.loc[tecnologia["roe"].idxmax()][["ticker","setor","roe"]]

# (1,5) 11 - Faça a Magic Formula através dos indicadores Return on Capital (roc) e Earning Yield (ey) no dia 2024-04-01.
# Monte uma carteira de investimento com 10 ações baseado na estratégia Magic Formula.
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# response = requests.get(
#     f"{base_url}/bolsa/planilhao",
#     headers={"Authorization": f"Bearer {token}"},
#     params={"data_base": "2026-04-01"},
# )
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2NTEyNTM5LCJpYXQiOjE3NzM5MjA1MzksImp0aSI6ImIwNTU4OTQwMzgzYTRlMDlhNmFjMzIyYTk0OGYwM2UxIiwidXNlcl9pZCI6Ijk4In0.vpr-Le2G9XHbJsykBktBJ6FI6P1qq5L0a31DLQMBoV0"
response = requests.get(
     f"{base_url}/bolsa/planilhao",
     headers={"Authorization": f"Bearer {token}"},
     params={"data_base": "2026-04-01"},
)
df = pd.DataFrame(response.json())
df = df[["ticker","roc","earning_yield","setor"]].dropna()
df["rank_roc"] = df["roc"].rank(ascending=False)
df["rank_ey"] = df["earning_yield"].rank(ascending=False)
df["magic_score"] = df["rank_roc"] + df["rank_ey"]
carteira = df.sort_values("magic_score").head(10)

# (1,5) 12 - Quantos setores ("setor") tem essa carteira formada por 10 ações?

setores_carteira = carteira["setor"].nunique()

