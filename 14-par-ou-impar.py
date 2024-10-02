def par(x):
    return x % 2 == 0


def par_ou_ímpar(x):
    if par(x):
        return "par"
    else:
        return "ímpar"


valor = 0 
while valor != 'S':
    valor = input("Digite um valor ou 'S' para sair: ")
    if valor != 'S':
        print(par_ou_ímpar(int(valor)))
    else:
        print("Fim do programa")
        