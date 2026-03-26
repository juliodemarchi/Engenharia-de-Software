#include <stdio.h>

int main() {
    
    int idade = 20;
    float altura = 1.75;
    
    //idade >= 18 => Verdadeira
    //idade <= 30 => Verdadeira
    //Verdadeira && Verdadeira
    //Verdadeiro && altura . 1.70
    //Verdadeiro && Verdadeiro = > verdadeiro.

    if (idade >= 18 && idade <= 30 && altura > 1.70) {
        printf("Voce esta na faixa etaria e tem a altura adequada\n");
    } else {
        printf("Voce não atende os critérios\n");
    }

}