#include <stdio.h>

 int main () {
    int idade = 25;
    int quantidade = 1;
    float altura = 1.75;
    char opcao = 'A';
    char nome [20] =  "sergio";
    
    printf("Digite a sua idade: ");
    scanf("%d", &idade);
    printf("A idade é: %d\n", idade);

    printf("Digite sua altura; ");
    scanf("%f", &altura);
    printf("A altura é: %f", altura);


    /*
    printf("%fromato1 %formato2 %formato3", variavel1, variavel2, variavel3)
    
    %d: Imprime um inteiro no formato decimal.
    %i: Equivalente a %d.
    %f: Imprime um número de ponto flutuante no formato padrao.
    %e: Imprime um número de ponto flutuante na notação científica.
    %c: Imprime um único caractere.
    %s: Imprime uma cadeia (string) de caracteres.

    */
  


}