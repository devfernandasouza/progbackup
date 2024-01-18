def fatorial(valor):
    fatorial = 1

    if (valor == 0 or valor == 1):
        return valor
    else:
        for i in range(1, valor+1):
            fatorial = fatorial * i
        return fatorial

def main():

    valor = int(input("Insira um valor para calcular o fatorial: "))
    fatorial(valor)

if __name__ == '__main__':
    main()