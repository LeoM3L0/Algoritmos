def regressiva_infinita(i): ## Esta Recurssão não tem fim pois não tem caso base ou condição de parada
    print(i) ## Ou seja, ficara chamando a função infinitamente
    regressiva_infinita(i - 1)

## print(regressiva(100))

def regressiva(i): ## Esta Recurssão tem fim pois tem caso base ou condição de parada
    if i == 0:
        print("Fim Da Contagem")
        return
    else: ## E também tem o caso recursivo ou seja, a condição de chamada da função novamente
        print(i)
        regressiva(i - 1)

print(regressiva(100))