#include <stdio.h>

int main() {
    int num1 = 40, num2 = 20;
    int maior;


    num1 > num2 ? (maior = num1) : (maior = num2);
    printf("O numero maior é: %d", maior);

    if (num1 > num2)
    {
        printf("O numero maior é %d\n", num1);
    } else {
        printf("O numero maior é %d\n", num2);
    }
    


    
    return 0;

}