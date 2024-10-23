# Solicitar que o usuário insira um número
numero = int(input("Digite um número: "))

# Verifica se o número é primo 
def e_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Exibir o resultado
if e_primo(numero):
    print(f"{numero} é um número primo.")
else: 
    print(f"{numero} não é um número primo.")