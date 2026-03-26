#include <stdio.h>


int main () {
    
    char codigo1[5]= "A01", codigo2 [5]= "B02", codigo3 [5]= "C03"; /*codigo para pesquisar sobre os estados*/
    char estado1[20]= "Rondonia", estado2 [20]= "Ceara", estado3 [20]= "Sao paulo"; /*Nomes dos estados*/
    char cidade1[20]= "Porto Velho", cidade2[20]= "Fortaleza", cidade3[20]= "Sao Paulo"; //nomes das capitais dos estados
    int populacao1 = 1746227, populacao2 = 8790000, populacao3 = 46000000; //populacao dos estados
    int area1 = 237590, area2 = 146348 , area3 = 248209; //areas da terra
    float PIB1 = 76, PIB2 = 2.5, PIB3 = 3.5; //PIB dos estados, bruto, 2023
    int turismo1 = 15, turismo2 = 55, turismo3 = 2000; //pontos turisticos nao existe uma quantidade precisa



    printf ("Codigo da Carta: %s\n", codigo1); // reprodução do codigo da carta
    printf ("Nome: %s\n", estado1); //reprodução do nome do estado
    printf ("Capital do estado: %s\n", cidade1); //reprodução da capital do estado
    printf ("População: %d\n", populacao1); //quantidade de habitantes na região
    printf ("Dimensão de area: %d\n", area1);
    printf ("PIB interno bruto: %2.f bilhões\n", PIB1);
    printf ("Locais de turismo: %d\n\n\n", turismo1);

    printf ("Codigo da Carta: %s\n", codigo2); // reprodução do codigo da carta
    printf ("Nome: %s\n", estado2); //reprodução do nome do estado
    printf ("Capital do estado: %s\n", cidade2); //reprodução da capital do estado
    printf ("População: %d\n", populacao2); //quantidade de habitantes na região
    printf ("Dimensão de area: %d\n", area2);
    printf ("PIB interno bruto: %.2f bilhões\n", PIB2);
    printf ("Locais de turismo: %d\n\n\n", turismo2);

    printf ("Codigo da Carta: %s\n", codigo3); // reprodução do codigo da carta
    printf ("Nome: %s\n", estado3); //reprodução do nome do estado
    printf ("Capital do estado: %s\n", cidade3); //reprodução da capital do estado
    printf ("População: %d\n", populacao3); //quantidade de habitantes na região
    printf ("Dimensão de area: %d\n", area3); // dimensao de area
    printf ("PIB interno bruto: %.2f trilhões\n", PIB3); // PIB anual do estado
    printf ("Locais de turismo: %d\n\n\n", turismo3); //locais para turismo
    



    return 0;

}