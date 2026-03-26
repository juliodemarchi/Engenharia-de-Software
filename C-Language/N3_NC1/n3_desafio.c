#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h> // Adicionado para facilitar a comparação de letras

int main() {
    int resultado1 = 0, resultado2 = 0;
    char primeiroAtributo, segundoAtributo;
    int ataque1, ataque2, defesa1, defesa2, recuo1, recuo2;

    srand(time(0));
    // Simulando valores aleatórios (removendo os fixos para testar)
    ataque1 = rand() % 100 + 1; ataque2 = rand() % 100 + 1;
    defesa1 = rand() % 100 + 1; defesa2 = rand() % 100 + 1;
    recuo1 = rand() % 100 + 1;  recuo2 = rand() % 100 + 1;

    printf("--- JOGO DE ATRIBUTOS ---\n");
    printf("Escolha o primeiro atributo (A, D ou R): ");
    scanf(" %c", &primeiroAtributo);
    primeiroAtributo = toupper(primeiroAtributo); // Converte para maiúsculo

    switch (primeiroAtributo) {
        case 'A': resultado1 = (ataque1 > ataque2); break;
        case 'D': resultado1 = (defesa1 > defesa2); break;
        case 'R': resultado1 = (recuo1 > recuo2); break;
        default: printf("Opção inválida!\n"); return 1;
    }

    printf("\nEscolha o segundo atributo (diferente do primeiro): ");
    scanf(" %c", &segundoAtributo);
    segundoAtributo = toupper(segundoAtributo);

    if (primeiroAtributo == segundoAtributo) {
        printf("Erro: Você escolheu o mesmo atributo!\n");
    } else {
        switch (segundoAtributo) {
            case 'A': resultado2 = (ataque1 > ataque2); break;
            case 'D': resultado2 = (defesa1 > defesa2); break;
            case 'R': resultado2 = (recuo1 > recuo2); break;
            default: printf("Opção inválida!\n"); return 1;
        }

        // --- EXIBIÇÃO DO RESULTADO FINAL ---
        printf("\n--- PLACAR FINAL ---\n");
        int total = resultado1 + resultado2;
        
        if (total == 2) printf("Vitória Total! Você venceu nos dois atributos.\n");
        else if (total == 1) printf("Empate Técnico! Venceu em um e perdeu no outro.\n");
        else printf("Derrota! Você perdeu em ambos.\n");
    }

    return 0;
}