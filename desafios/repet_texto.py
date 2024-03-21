# Agora vamos solicitar uma string e um numero inteiro como entrada. Depois teremos que repetir a string o numero de vezes que foi informado no número inteiro

string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

print((string + '\n') * numero, end='')