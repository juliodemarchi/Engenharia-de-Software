#include <stdio.h>

int main(){

    int idade;

    printf("Digite a sua idade: ");
    scanf("%d", &idade);

    //Criança menor < 12
    //Adolescente 12 <= x < 18
    //Adulto 18 <= x < 60
    //Idoso > 60

    if (idade < 12){
        printf("Voce é uma criança!\n");
    } else if (idade >= 12 && idade < 18){
        printf("Voce é um adolescente!\n");
    } else if (idade >= 18 && idade < 60){
        printf("Voce é um adulto!\n");
    } else {
        printf("Voce é um idoso\n");
    }

}