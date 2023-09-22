#a

def contagem_regressiva(numero):
    for i in range(numero, 0, -1):
        print(i)
    print("Contagem regressiva concluída!")

try:
    numero = int(input("Digite um número inteiro para a contagem regressiva: "))
    contagem_regressiva(numero)
except ValueError:
    print("Por favor, insira um número inteiro válido.")


#b

def soma_recursiva(numero):
    if numero <= 1:
        return 1
    else:
        return numero + soma_recursiva(numero - 1)

try:
    numero = int(input("Digite um número inteiro para calcular a soma recursiva até 1: "))
    if numero <= 0:
        print("O número deve ser maior que 0.")
    else:
        resultado = soma_recursiva(numero)
        print(f"A soma recursiva até 1 é: {resultado}")
except ValueError:
    print("Por favor, insira um número inteiro válido.")


#c

def inverter_string(string):
    return string[::-1]

try:
    entrada = input("Digite uma string para inverter: ")
    string_invertida = inverter_string(entrada)
    print(f"A string invertida é: {string_invertida}")
except:
    print("Ocorreu um erro :(")