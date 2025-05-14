2 - Crie um programa que solicite um número ao usuário e exiba a tabuada desse número de 1 a 10, utilizando a estrutura de repetição for.

numero = int(input("Digite um número para ver a tabuada: "))
print(f"\A tabuada do número{numero}: ")
for i in range(1, 11):
    print(f"{numero}* {i} = {numero * i}")