# Exibindo números de 1 a 10 com uma mensagem personalizada
for numero in range(1, 11):
    print(f"Número atual: {numero}")

    # Gerando uma saída com 1000 linhas
for i in range(1, 1001):
    print(f"Esta é a linha número {i}")

    # Função que retorna o dobro de um número
def dobro(numero):
    return numero * 2

# Solicitar um número ao usuário
num = int(input("1 a 55: "))

# Chamar a função e exibir o resultado
resultado = dobro(num)
print(f"O dobro de {num} é {resultado}")