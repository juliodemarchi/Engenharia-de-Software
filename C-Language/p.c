#include <stdio.h>

// Definição de uma função (Modularização)
void saudar() {
    printf("Olá, Mundo!\n");
}

int main() {
    // Paradigma Imperativo: Execução passo a passo
    int contador = 0; 
    
    while(contador < 3) {
        saudar();
        contador++; // Alteração de estado
    }
    
    return 0;
}
