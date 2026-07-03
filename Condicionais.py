nome = input("Digite o seu nome: ")
print(nome, '\n')

# PEDINDO IDADE (str) E JÁ INDICANDO A CONVERSÃO PARA int
idade = int(input("Digite sua idade: "))
print(idade, '\n')

if (idade >= 18):
    print(f"O {nome} pode acessar o sistema")
    print(f"Ele tem {idade} anos.")
else:
    print(f'O {nome} não pode acessar o sistema')
    print(f"Ele tem {idade} anos.")

print('===== PROGRAMA ENCERRADO ===== \n')

media = float(input("Digite a media das suas notas: "))

if media >= 7.0:
    print(f"Parabéns {nome}! Você foi aprovado!")
elif media >= 5 and media < 7.0:
    print(f"{nome}, você está de recuperação")
else:
    print(f"{nome}, você foi reprovado!")