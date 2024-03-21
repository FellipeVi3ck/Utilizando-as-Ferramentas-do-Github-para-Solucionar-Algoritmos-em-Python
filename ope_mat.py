# Vamos solicitar como entrada dois numeros e depois vamos realizar uma operação simples entre eles

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

operacao = input("Digite a operaçao que deseja realizar: ")

if operacao == '+':
    print(numero1 + numero2)

elif operacao == '-':
    print(numero1 - numero2)

elif operacao == '*':
    print(numero1 * numero2)

elif operacao == '/':
    print(numero1 / numero2)

else:
    print("Operação inválida!")

print("O resultado desejado é", operacao)