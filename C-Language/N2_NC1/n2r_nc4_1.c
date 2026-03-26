#include <stdio.h>

int main() {
    int variavel;

    printf("Digite um valor\n");
    scanf("%d", &variavel);

    switch (variavel) {
        case 1:
        printf("Código a ser executado se a variavel == 1\n");
        printf("Teste do case 1");
        break;

        case 2:
        printf("Código a ser executado se a variavel == 2\n");
        break;
        
        default:
        printf("Código a ser executado se a variavel não for 1 ou 2\n");
    }

    

}