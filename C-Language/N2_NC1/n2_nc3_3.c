#include <stdio.h>

int main () {
    /*
    Incremento (++)
    Pré-Incremento ++a
    Pós-Incremento a++
    Decremento (--)
    Pré-Decremento --a
    Pós-Decremento a--
    */

    int numero1 = 1, resultado;

    printf("Antes incremento: %d\n", numero1);
    //numero1 = numero1 +1;
    //numero1 += 1;
    //Pos incremento;
    //resultado = numero1;
    //numero++;

    resultado = numero1++;
    //printf("Apos incremento: %d\n", numero1);
    printf("Apos Pós-incremento - numero1: %d - Resultado: %d\n", numero1, resultado);

    resultado = ++numero1;
    //printf("Apos incremento: %d\n", numero1);
    printf("Apos Pre-incremento - numero1: %d - Resultado: %d\n", numero1, resultado);

    resultado = numero1--;
    //printf("Apos incremento: %d\n", numero1);
    printf("Apos Pre-incremento - numero1: %d - Resultado: %d\n", numero1, resultado);

    resultado = --numero1;
    //printf("Apos incremento: %d\n", numero1);
    printf("Apos Pre-incremento - numero1: %d - Resultado: %d\n", numero1, resultado);

    //numero1 - numero 1 - 1;
    //numero1 -= 1;
    //numero1--;
    //printf("Apos decremento: %d\n", numero1);

}
