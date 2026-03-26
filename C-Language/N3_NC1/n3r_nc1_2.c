#include <stdio.h>

int main() {
    int temperatura = 28;
    int resultado;


    resultado = temperatura > 30 ? 1 : 0;
    if (resultado == 1)
    {
        printf("Esta Calor!\n");
    } else {
        printf("Esta frio!\n");

    }


    
    return 0;

}