import os
from google import genai

#PASSANDO A CHAVE PARA O PROGRAMA
api_key = os.getenv("GOOGLE_API_KEY_AMEPA")

if not api_key: #Verifica se api key foi encontrada ou está vazia
    raise RuntimeError(f"A variável {api_key} não foi encontrada")

#Cria um clinete da API Gemini
client = genai.Client(api_key=api_key)

resposta = client.models.generate_content(model="gemini-2.5-flash", contents="O que é uma IA?")
print(resposta.text)


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