def main():
    a = input()
    vet = []
    tamanho = len(a)

    for i in range(tamanho):
        vet.append(a[i])
    for i in range (tamanho//2 , 0, i-1):
        print(vet[i])

if __name__ == "__main__":
    main()
