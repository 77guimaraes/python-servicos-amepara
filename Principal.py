import os
from google import genai

# PASSANDO A CHAVE PARA O PROGRAMA
api_key = os.getenv("GEMINI_API_KEY_PESSOAL")

# Verifica se a API Key foi encontrada ou está vazia
if not api_key:raise RuntimeError("A variável GEMINI_API_KEY_PESSOAL não foi encontrada.")

# Cria um cliente da API Gemini
client = genai.Client(api_key=api_key)

# Cria o chatbot
chat = client.chats.create(model="gemini-2.5-flash")

# Envia uma mensagem para o chatbot
resposta = chat.send_message("O que é o Python?")
print(resposta.text) # Exibe a resposta
historico = chat.get_history() # Exibe o histórico

# para cada mensagem dentro de histórico, imprima a mensagem.
for mensagem in historico:
    print(mensagem)



# produto1 = 5
# produto2 = 2000
# print (produto1 + produto2, '\n')
#
# nomeProduto1 = 'Sandalia'
# nomeProduto2 = 'Meia'
# nomeProduto3 = 'Celular'
# print (nomeProduto1, nomeProduto2, nomeProduto3, '\n')
#
# amigos = 6
# aluguel = 1000
# supermercado = 500
# carro = 400
# total = aluguel + supermercado + carro
# print(total, '\n')
#
# print('Amigo: ', amigos)
# print('Akuguel dos carros: ', carro * 2)
# totalCarros = carro * 2
# print(totalCarros, '\n')
#
# total2 = (aluguel + supermercado + totalCarros)
# print(total2, '\n')
#
# totalPorPessoa = total2 / amigos
# print(totalPorPessoa, '\n')
#
# #PEDINDO O TIPO DA VARIÁVEL
# type (totalPorPessoa)
# print(type(totalPorPessoa), '\n')
#
# pedroTemCNH = True
# joaoTemCNH = False
# print(type(pedroTemCNH), '\n')
#
# texto1 = "   Irã Morrison --- Analista de Sistemas  "
# print(texto1, '\n')
# print(texto1.lower(), '\n') #IMPRIME TUDO EM LETRA MINÚSCULA
# print(texto1.upper(), '\n') #IMPRIME TUDO EM LETRA MAIÚSCULA
# print(texto1.strip(), '\n') #REMOVE OS ESPAÇOS EXTRAS
# print(texto1.split(), '\n') #COLOCA ENTRE '' TODOS OS CONJUNTOS DE CARACTERES
# print(texto1.replace(' ', '.')) #SUBSTITUI O PRIMEIRO CARACTERE INFORMADO PELO SEGUNDO CARACTERE INFORMADO
# print(texto1.strip().upper().replace(' ', '.'), '\n') #JUNTANDO FUNÇÕES