def soma(vetor1, vetor2):
    vetorzao = vetor1 + vetor2
    acumulativa = 0
    # valor <- 1,1,1,1,1,3,2
    for valor in vetorzao:
        acumulativa = acumulativa + valor
        print(valor)
    return acumulativa
        

# main
vet = [1,1,1,1,1]
vet2 = [3,2]
resultado = soma(vet, vet2)
#soma(vet2)
print(resultado) 