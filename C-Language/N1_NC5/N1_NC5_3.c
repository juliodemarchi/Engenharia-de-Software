#include <stdio.h>

 int main () {
    int idade;
    float altura;
    char opcao;
    char nome[20];

    // sintaxe scanf
    // scanf("formato1" "formato2", &variavel1, variavel2, ...);

    printf("Digite a sua idade: ");
    scanf("%d", &idade);
    printf("A sua idade é: %d anos. \n", idade);

    printf("Digite a sua altura: \n");
    scanf("%f", &altura);
    printf("A sua altura é: %f metros.\n", altura);

    printf("Digite seu nome: \n");
    scanf(" %s", nome);
    printf("Seu nome é: %s\n", nome); 

    printf("Informe sua letra chave: \n");
    scanf(" %c", &opcao);
    printf("Sua letra chave é: %c\n", opcao); 

    /*
    printf("%formato1 %formato2 %formato3", variavel1, variavel2, variavel3)
    %d: imprime um inteiro no formato decimal.
    %i: Equivalente a %d.
    */

 }    