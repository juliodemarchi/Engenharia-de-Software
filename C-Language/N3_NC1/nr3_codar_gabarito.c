#include <time.h>

int main () {
    int numeroJogador, numeroComputador, resultado;
    char tipoComparacao;
    
    //Gerar numero aleatorio
    srand(time(0));
    numeroComputador = rand() % 100 + 1; //Numero entre 1 e 100

    //Inicio do jogo
    printf("Bem-vindo ao jogo Maior, Menor ou igual!\n");
    printf("Voce deve escolher um numero e o tipo de comparação.\n");
    printf("M. Maior\n");
    printf("N. Menor\n");
    printf("T. Igual\n");

    printf("Escolha a comparação: \n");
    scanf(" %c", &tipoComparacao);

    printf("Digite seu numero (entre 1 e 100): ");
    scanf("%d", &numeroJogador);

    //Exibir numero do computador
    //printf("O numero do computador é: %d\n", numeroComputador);

    switch (tipoComparacao)
    {
    case 'M':
    case 'm':
        printf("Você escolheu a opção maior!\n");
        resultado = numeroJogador > numeroComputador ? 1 : 0;
        break;
    
    case 'N':
    case 'n':
        printf("Você escolheu a opção menor!\n");
        resultado = numeroJogador < numeroComputador ? 1 : 0;
        break;
    
    case 'I':
    case 'i':
        printf("Você escolheu a opção igual!\n");
        resultado = numeroJogador == numeroComputador ? 1 : 0;
        break;

    default:
        printf("Opção de jogo inválida!\n");
        break;
    }

    printf("O numero do computador é: %d e o jogador é: %d\n", numeroComputador, numeroJogador);

    if (resultado == 1)
    {
        printf("Parabens! Voce venceu!\n");
    } else {
        printf("Infelizmente voce perdeu!\n");
    }
    

}