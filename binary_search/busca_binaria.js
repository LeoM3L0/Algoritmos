function buscaBinaria(array, alvo) {
    let inicio = 0;
    let fim = array.length -1;

    while (inicio <= fim) {
        // Calculo do índice meio
        let meio = Math.floor((inicio + fim) / 2);

        if(array[meio] === alvo){
            return meio; // Encontrou o elemento
        }
        else if(array[meio] < alvo) {
            inicio = meio + 1; // Procura na metade Direita
        }
        else {
            fim = meio - 1; // Procura na metadade Esquerda
        }
    }
    return -1; // Elemento não encontrato
}

