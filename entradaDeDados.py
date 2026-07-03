nome = input("Digite o seu nome: ")
print(nome, '\n')
idade = input ("Digite sua idade: ")

print(idade, '\n')

print('ANTES DA CONVERSÃO: ', type(idade), type(nome), '\n')

#CONVERTENDO TIPO DA VARIÁVEL
idade = int(idade)
print('DEPOIS DA CONVERSÃO: ', type(idade), type(nome), '\n')

#PRINT COM VÍRGULAS
print("O usuário se chama", nome,"e tem", idade, "anos de idade")

#PRINT CONCATENANDO (NÃO É POSSÍVEL CONCATENAR int COM str)
print("O usuário se chama " + nome + " e tem", str(idade), "anos de idade")

#PRINT COM f E CHAVEZ NAS VARIÁVEIS
print(f"O usuário se chama {nome} e tem {idade} anos de idade")

