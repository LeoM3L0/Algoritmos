def saudacao(nome): 
    print(f"Olá {nome}!") # Primeiro o computador aloca memória para a função saudacao
    saudacao2(nome) # Depois e adiconado ao topo da pilha de chamadas a alocação de memória para a função saudacao2 e depois de excutada e removida
    print("Despedindo!") # Por fim, e adicionado ao topo da pilha a chamada da função tchau
    tchau() # Depois de executada, a função tchau é removida da pilha e então a função saudacao é removida da pilha
    return "Finalizado Call Stack de Saudações"

def saudacao2(nome):
    print(f"Tudo bem {nome}?")

def tchau():
    print("Tchau, até mais!")

print(saudacao("Leo"))