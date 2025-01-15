# Importar a base de dados 
# visualizar a base de dados (entender a base e identificar problemas)
# -> informações que tem de cada cliente, e solucionar os problemas
# corrigir problemas da base de dados (tratamento de dados)
# analise inicial -> quantos cliente cancelaram e qual o % de cliente 
# analise da causa de cnacelamento dos clientes

# !pip install pandas numpy poenpyxl nbformat ipykernel plotly

# Importar a base de dados 
# pd (apelido que da para o pandas)
import pandas as pd 
import display

tabela = pd.read_csv("cancelamnetos_sample.csv") # o nome tabela é uma variavel / pode passar link tbm caso esteja em uma maquina virtual

# visualizar a base de dados (entender a base e identificar problemas)
# -> informações que tem de cada cliente, e solucionar os problemas

# drop é usado para eliminar, neste caso eliminou a coluna 
tabela = tabela.drop(columns="CustumerID")

display(tabela) # é melhor usar o display do que o print, pois fica melhor para visualizar as informações

# corrigir problemas da base de dados (tratamento de dados)
# float -> numero com casa decimal
# object -> coluna com valores de texto
# valores vazios -> deletar linhas com valores vazios 
display(tabela.info()) # ver as informações da tabela 

tabela = tabela.dropna() # NaN -> Not a Number = Valores vazios 

display(tabela.info())

# analise inicial -> quantos cliente cancelaram e qual o % de cliente 
# contar na coluna cancelou os valores
tabela["cancelou"].value_counts() # toda lista é passada entre colchetes

display(tabela["assinatura"].value_counts())

# para calcular a média, não é muito diferente, deve trocar apenas o counts por mean 
display(tabela["assinatura"].value_mean())

# fornecer as informações em porcentagem 
display(tabela["assinatura"].value_counts(normalize=True))

# 0 = falso e 1 = verdadeiro

# analise da causa de cnacelamento dos clientes
# color_discrete_map -> usado para especificar a cor que você quer 
# (comparar as outras colunas da tabela com a coluna de cancelamento)
import plotly.express as px # express pois ele ja trás gráficos "prontos"

# criar o gráfico
coluna = "assinatura"

# EXEMPLO
# for item in lista 
    # todos os codigos que estiverem aqui 
    # ele vai executar, para cada item da lista 
    # (jeito de selecionar os itens da lista, sem precisar escrever um por um)


for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou", text_auto=True)

    # exibir o gráfico
    grafico.show()

# usuarios do contrato mensal sempre cancelam
    # evitar o contrato mensal e incentivar (com desconto) os contratos anuais e trimestrais 

# todos os usuarios que ligaram mais de 4x para o call center, cancelaram o serviço
    # criar um processo que quando um usuario bateu 3 ligações para o call center, alerta vermelho 

# usuarios que atrasarem o pagamento mais de 20 dias, cancelaram
    # criar um alerta para quando o atraso do pagamento bater 15 dias, entrar em contato

# duracao_contrato -> diferente de mensal
condicao = tabela[duracao_contrato] != "Monthy"

tabela = tabela[condicao]

# -------------------- OU ------------

tabela = tabela[[duracao_contrato] != "Monthy"]

# ligacoes_callcenter -> menor ou igual a 4
tabela = tabela[tabela["ligacoes_callcenter"] <= 4]

# dias_atraso <= 20 dias
tabela = tabela[tabela["dias_atraso"]<=20]

display(tabela["cancelou"].value_counts())

# percentual
display(tabela["cancelou"].value_counts(normalize=True))