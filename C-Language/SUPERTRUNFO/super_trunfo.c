#include <stdlib.h>
#include <stdio.h>
#include <locale.h>
#include <string.h>

int main()
{
    setlocale(LC_ALL, "Portuguese"); // Configura a linguagem para português (acentos, caracteres especiais)

    // Declaração das variáveis para armazenar dados das duas cidades
    char estado1[2], estado2[2];           // Armazena a letra do estado de cada cidade
    char cidade1[20], cidade2[20];         // Armazena o nome das cidades
    float pib1, area1, pib2, area2;        // PIB e área de cada cidade
    float pibPerCapita1, pibPerCapita2;    // PIB per capita calculado para cada cidade
    float densidade1, densidade2;          // Densidade populacional calculada
    unsigned int densidadePibPerCapita1, densidadePibPerCapita2; // Variáveis auxiliares para comparação (não usadas diretamente)
    unsigned int populacao1, populacao2;   // População das cidades
    int pontosTuristicos1, pontosTuristicos2; // Número de pontos turísticos
    int escolhaAtributo1, escolhaAtributo2;   // Escolha do usuário dos atributos a comparar
    int carta1 = 1, carta2 = 2;            // Identificadores das cartas
    int resultadoCarta;                     // Variável para mostrar os resultados das cartas
     
    // Protótipo da função compararAtributo (não utilizada no código atual)
    void compararAtributo(int escolha, char cidade1[20], char cidade2[20],
                      int populacao1, int populacao2,
                      float area1, float area2,
                      float pib1, float pib2,
                      int pontosTuristicos1, int pontosTuristicos2,
                      float densidade1, float densidade2,
                      float pibPerCapita1, float pibPerCapita2);

    // ******************************* Entrada de dados da Carta 1 *******************************
    printf("***************  CARTA 1  ***************\n");

    // Lê o nome da cidade com fgets para permitir nomes compostos
    printf("Digite o nome da cidade em que você mora:\n");
    fgets(cidade1, sizeof(cidade1), stdin); 
    cidade1[strcspn(cidade1, "\n")] = 0; // Remove o '\n' lido pelo fgets

    // Lê a letra do estado
    printf("Digite a letra do seu Estado entre 'A' e 'H'\n");
    scanf("%s", estado1);

    // População
    printf("Digite o número total de população que existe na sua cidade:\n");
    scanf("%d", &populacao1);

    // Área
    printf("Digite o número da Área em Km² da cidade em que você mora:\n");
    scanf("%f", &area1);

    // PIB
    printf("Digite o PIB Anual da sua cidade: \n");
    scanf("%f", &pib1);

    // Pontos turísticos
    printf("Digite o número de pontos turisticos que existe em sua cidade:\n");
    scanf("%d", &pontosTuristicos1);

    // Calcula densidade populacional e PIB per capita
    densidade1 = (float)populacao1 / area1;
    pibPerCapita1 = (float)pib1 / populacao1;

    // ******************************* Entrada de dados da Carta 2 *******************************
    getchar(); // Limpa o buffer do teclado (sobrou o '\n' do scanf anterior)
    printf("***************  CARTA 2  ***************\n");

    // Lê o nome da cidade destino
    printf("Digite o nome da cidade pra onde você quer viajar:\n");
    fgets(cidade2, sizeof(cidade2), stdin); 
    cidade2[strcspn(cidade2, "\n")] = 0; // Remove o '\n' lido pelo fgets

    // Lê o estado da segunda cidade
    printf("Digite a letra do segundo estado entre 'A' e 'H' (Não pode ser igual ao estado anterior)\n");
    scanf("%s", estado2);

    // População, área, PIB e pontos turísticos da segunda cidade
    printf("Digite o número total de população que existe nessa cidade: \n");
    scanf("%d", &populacao2);

    printf("Digite o número da Área total em Km² dessa cidade: \n");
    scanf("%f", &area2);

    printf("Digite o PIB anual dessa cidade: \n");
    scanf("%f", &pib2);

    printf("Digite a quantidade de pontos turisticos que existem nessa cidade: \n");
    scanf("%d", &pontosTuristicos2);

    // Calcula densidade populacional e PIB per capita da segunda cidade
    densidade2 = (float)populacao2 / area2;
    pibPerCapita2 = (float)pib2 / populacao2;

    // Comparações auxiliares para densidade + PIB per capita (não utilizadas diretamente)
    densidadePibPerCapita1 = (float)(densidade1 + pibPerCapita1) > (densidade2 + pibPerCapita2);
    densidadePibPerCapita2 = (float)(densidade2 + pibPerCapita2) > (densidade1 + pibPerCapita1);

    // ******************************* Menu de escolha de atributos *******************************
menu_jogo:
    printf("Escolha 2 atributos para comparar entre as cartas e saber quais foram os vencedores\n");
    printf("1 - POPULAÇÃO\n");
    printf("2 - ÁREA EM Km²\n");
    printf("3 - PIB\n");
    printf("4 - NUMERO DE PONTOS TURISTUCOS\n");
    printf("5 - DENSIDADE DEMOGRÁFICA\n");
    printf("6 - PIB PER CAPITA\n");
    scanf("%d", &escolhaAtributo1);

    // Comparação do primeiro atributo
    switch (escolhaAtributo1)
    {
        case 1: // População
            printf("\nComparando População:\n");
            if (populacao1 > populacao2)
                printf("%s vence com %d habitantes contra %d de %s\n", cidade1, populacao1, populacao2, cidade2);
            else if (populacao2 > populacao1)
                printf("%s vence com %d habitantes contra %d de %s\n", cidade2, populacao2, populacao1, cidade1);
            else
                printf("Empate: %s e %s têm a mesma população (%d)\n", cidade1, cidade2, populacao1);
            break;

        case 2: // Área
            printf("\nComparando Área:\n");
            if (area1 > area2)
                printf("%s vence com %.2f km² contra %.2f km² de %s\n", cidade1, area1, area2, cidade2);
            else if (area2 > area1)
                printf("%s vence com %.2f km² contra %.2f km² de %s\n", cidade2, area2, area1, cidade1);
            else
                printf("Empate: %s e %s têm a mesma área (%.2f km²)\n", cidade1, cidade2, area1);
            break;

        case 3: // PIB
            printf("\nComparando PIB:\n");
            if (pib1 > pib2)
                printf("%s vence com %.2f bilhões contra %.2f bilhões de %s\n", cidade1, pib1, pib2, cidade2);
            else if (pib2 > pib1)
                printf("%s vence com %.2f bilhões contra %.2f bilhões de %s\n", cidade2, pib2, pib1, cidade1);
            else
                printf("Empate: %s e %s têm o mesmo PIB (%.2f)\n", cidade1, cidade2, pib1);
            break;

        case 4: // Pontos turísticos
            printf("\nComparando Pontos Turísticos:\n");
            if (pontosTuristicos1 > pontosTuristicos2)
                printf("%s vence com %d pontos turísticos contra %d de %s\n", cidade1, pontosTuristicos1, pontosTuristicos2, cidade2);
            else if (pontosTuristicos2 > pontosTuristicos1)
                printf("%s vence com %d pontos turísticos contra %d de %s\n", cidade2, pontosTuristicos2, pontosTuristicos1, cidade1);
            else
                printf("Empate: %s e %s têm o mesmo número de pontos turísticos (%d)\n", cidade1, cidade2, pontosTuristicos1);
            break;

        case 5: // Densidade demográfica (menor vence!)
            printf("\nComparando Densidade Demográfica:\n");
            if (densidade1 < densidade2)
                printf("%s vence com densidade %.2f contra %.2f de %s\n", cidade1, densidade1, densidade2, cidade2);
            else if (densidade2 < densidade1)
                printf("%s vence com densidade %.2f contra %.2f de %s\n", cidade2, densidade2, densidade1, cidade1);
            else
                printf("Empate: %s e %s têm a mesma densidade (%.2f)\n", cidade1, cidade2, densidade1);
            break;

        case 6: // PIB per capita
            printf("\nComparando PIB per capita:\n");
            if (pibPerCapita1 > pibPerCapita2)
                printf("%s vence com %.2f contra %.2f de %s\n", cidade1, pibPerCapita1, pibPerCapita2, cidade2);
            else if (pibPerCapita2 > pibPerCapita1)
                printf("%s vence com %.2f contra %.2f de %s\n", cidade2, pibPerCapita2, pibPerCapita1, cidade1);
            else
                printf("Empate: %s e %s têm o mesmo PIB per capita (%.2f)\n", cidade1, cidade2, pibPerCapita1);
            break;

        default:
            printf("Escolha um atributo Válido !");
            goto menu_jogo; // Retorna ao menu se a escolha for inválida
            break;
    }

    // Lê o segundo atributo a ser comparado
        printf("Escolha o segundo atributo para comparar entre as cartas e saber quais foram os vencedores\n");
    do {
        printf("Escolha o segundo atributo (1-6): ");
        scanf("%d", &escolhaAtributo2);
        if (escolhaAtributo2 < 1 || escolhaAtributo2 > 6) {
            printf("Escolha inválida! Digite um número entre 1 e 6.\n");
        } else if (escolhaAtributo2 == escolhaAtributo1) {
            printf("Escolha inválida! O segundo atributo deve ser diferente do primeiro.\n");
        } else {
            break; // atributo válido, sai do loop
        }
    } while (1);

    // Comparação do segundo atributo
    switch (escolhaAtributo2)
    {
        case 1: // População
            printf("\nComparando População:\n");
            if (populacao2 > populacao1)
                printf("%s vence com %d habitantes contra %d de %s\n", cidade2, populacao2, populacao1, cidade1);
            else if (populacao1 > populacao2)
                printf("%s vence com %d habitantes contra %d de %s\n", cidade1, populacao1, populacao2, cidade2);
            else
                printf("Empate: %s e %s têm a mesma população (%d)\n", cidade2, cidade1, populacao1);
            break;

        case 2: // Área
            printf("\nComparando Área:\n");
            if (area2 > area1)
                printf("%s vence com %.2f km² contra %.2f km² de %s\n", cidade2, area2, area1, cidade1);
            else if (area1 > area2)
                printf("%s vence com %.2f km² contra %.2f km² de %s\n", cidade1, area1, area2, cidade2);
            else
                printf("Empate: %s e %s têm a mesma área (%.2f km²)\n", cidade2, cidade1, area1);
            break;

        case 3: // PIB
            printf("\nComparando PIB:\n");
            if (pib2 > pib1)
                printf("%s vence com %.2f bilhões contra %.2f bilhões de %s\n", cidade2, pib2, pib1, cidade1);
            else if (pib1 > pib2)
                printf("%s vence com %.2f bilhões contra %.2f bilhões de %s\n", cidade1, pib1, pib2, cidade2);
            else
                printf("Empate: %s e %s têm o mesmo PIB (%.2f)\n", cidade2, cidade1, pib1);
            break;

        case 4: // Pontos turísticos
            printf("\nComparando Pontos Turísticos:\n");
            if (pontosTuristicos2 > pontosTuristicos1)
                printf("%s vence com %d pontos turísticos contra %d de %s\n", cidade2, pontosTuristicos2, pontosTuristicos1, cidade1);
            else if (pontosTuristicos1 > pontosTuristicos2)
                printf("%s vence com %d pontos turísticos contra %d de %s\n", cidade1, pontosTuristicos1, pontosTuristicos2, cidade2);
            else
                printf("Empate: %s e %s têm o mesmo número de pontos turísticos (%d)\n", cidade2, cidade1, pontosTuristicos1);
            break;

        case 5: // Densidade demográfica
            printf("\nComparando Densidade Demográfica:\n");
            if (densidade2 < densidade1)
                printf("%s vence com densidade %.2f contra %.2f de %s\n", cidade2, densidade2, densidade1, cidade1);
            else if (densidade1 < densidade2)
                printf("%s vence com densidade %.2f contra %.2f de %s\n", cidade1, densidade1, densidade2, cidade2);
            else
                printf("Empate: %s e %s têm a mesma densidade (%.2f)\n", cidade2, cidade1, densidade1);
            break;

        case 6: // PIB per capita
            printf("\nComparando PIB per capita:\n");
            if (pibPerCapita2 > pibPerCapita1)
                printf("%s vence com %.2f contra %.2f de %s\n", cidade2, pibPerCapita2, pibPerCapita1, cidade1);
            else if (pibPerCapita1 > pibPerCapita2)
                printf("%s vence com %.2f contra %.2f de %s\n", cidade1, pibPerCapita1, pibPerCapita2, cidade2);
            else
                printf("Empate: %s e %s têm o mesmo PIB per capita (%.2f)\n", cidade1, cidade2, pibPerCapita1);
            break;

        default:
            printf("Escolha um atributo Válido !");
            goto menu_jogo;
            break;
    }

    // ******************************* Menu para mostrar resultado das cartas *******************************
menu_resultado:
    printf("Deseja ver o resultado da carta? 1(Sim), 2(Não)\n");
    scanf("%d", &resultadoCarta);

    if (resultadoCarta == 1)
    {
        // Mostra todos os dados da primeira cidade
        printf("\n***************  SAÍDA DE DADOS DA PRIMEIRA CIDADE  ***************\n");
        printf("Carta nº %d \n", carta1);
        printf("Estado: %s \n", estado1);
        printf("Código: %s01 \n", estado1);
        printf("Nome da Cidade: %s\n", cidade1);
        printf("População: %d\n", populacao1);
        printf("Área: %.2f Km²\n", area1);
        printf("PIB: %.2fR$ Bilhões de Reais\n", pib1);
        printf("Número de Pontos Turísticos: %d\n", pontosTuristicos1);
        printf("A Densidade populacional da cidade %s é: %.2f hab/km²\n", cidade1, densidade1);
        printf("O PIB Per Capita da cidade de %s é: %.2fR$\n", cidade1, pibPerCapita1);

        // Mostra todos os dados da segunda cidade
        printf("\n***************  SAÍDA DE DADOS DA SEGUNDA CIDADE  ***************\n");
        printf("Carta nº %d\n", carta2);
        printf("Estado: %s \n", estado2);
        printf("Código: %s02 \n", estado2);
        printf("Nome da cidade: %s\n", cidade2);
        printf("População: %d\n", populacao2);
        printf("Área: %.2f Km²\n", area2);
        printf("PIB: %.2fR$ Bilhões de Reais\n", pib2);
        printf("A Densidade populacional da cidade %s é: %.2f hab/km²\n", cidade2, densidade2);
        printf("Número de Pontos Turísticos: %d\n", pontosTuristicos2);
        printf("O PIB Per Capita da cidade de %s é: %.2fR$\n", cidade2, pibPerCapita2);
        printf("\n***************  FIM DO JOGO DAS CARTAS SUPER TRUNFO  ***************\n");
    }
    else if (resultadoCarta == 2)
    {
        printf("Fim do jogo!\n"); // Encerramento do programa sem mostrar detalhes
    }
    else
    {
        printf("Escolha uma opção válida!\n");
        goto menu_resultado; // Retorna ao menu caso opção inválida
    }

    return 0; // Finaliza o programa
}