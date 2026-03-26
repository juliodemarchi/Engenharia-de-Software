#include <stdio.h>

int main () {
    /*
    Soma (+)
    Subtração (*)
    Divisão (/)
    */

    int numero1, numero2;
    int soma, subtracao, multiplicacao, divisao;

    printf("Entre com o numero 1: \n");
    scanf("%d", &numero1);
    printf("Entre com o numero 2: \n");
    scanf("%d", &numero2);
        
    soma = numero1 + numero2; // operação soma

    subtracao = numero1 - numero2; //operacao subtração

    multiplicacao = numero1 * numero2; // operação multiplicacao

    divisao = numero1 / numero2; // operacao divisao

    printf("A soma é: %d\n", soma);
    printf("A subtração é: %d\n", subtracao);
    printf("A multiplicacao é: %d\n", multiplicacao);
    printf("A divisao é: %d\n", divisao);






}