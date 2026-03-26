#include <stdio.h>
#include <locale.h>
#include <stdlib.h>
int main()
{
    setlocale(LC_ALL, "Portuguese_Brazil");
    int idade = 28;
    float altura = 1.63;
    char opcao = 'S';
    char nome[20] = "Regis";

    printf("O nome do usu�rio �: %s\n", nome);
    printf("A idade do usu�rio �: %d\n", idade);
    printf("A altura do usu�rio �: %.2f\n", altura);
    printf("A op��o �: %c\n", opcao);

    return 0;

    /*
    printf ("%formato1 %fomarto2 %fomarto 3", variavel1, variavel2, variavel3);

    %d: imprime um inteiro no formato decimal.
    %i: Equivalente a %d.
    %f: Imprime um n�mero de ponto flutuante no formato padr�o.
    %e: Imprime um n�mero de ponto flutuante na nota��o cient�fica.
    %c: Imprime um �nico caractere;
    %s: Imprime uma cadeia (string) de caracteres.
    */
}