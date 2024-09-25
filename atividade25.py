# Crie um programa que receba uma quantidade indefinida de números do usuário. O programa deve calcular a média desses números e parar quando o usuário digitar -1.
def calcular_media():
    soma = 0
    contador = 0
    
    while True:
        numero = float(input("Digite um número (-1 para sair): "))
        if numero == -1:
            break
        soma += numero
        contador += 1
    
    if contador > 0:
        media = soma / contador
        print(f"A média dos números digitados é: {media}")
    else:
        print("Nenhum número foi digitado.")

calcular_media()
