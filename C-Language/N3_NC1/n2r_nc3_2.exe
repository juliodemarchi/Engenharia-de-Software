#include <stdio.h>
int main(){
    int idade;
    int dependentes;
    float renda;

    // A primeira condição idade do usuario esta entre 18 e 65 anos.
    // A segunda condição se a renda do usuario é menor que 3000.
    // A terceira condicao verifica se o numero de dependentes é amior que 2.

printf("Digite a sua idade: ");
scanf("%d", &idade);
printf("Digite a sua renda mensal: ");
scanf("%f", &renda);
printf("Digite o numero de dependentes: ");
scanf("%d", &dependentes);

if(idade <= 18 && idade < 65){
    if (renda < 3000){
        if (dependentes > 2){
            printf("Voce atende a todos os criterios\n");
        } else {
            printf("Voce nao atende ao criterio dependentes\n");
        }
    } else {
        printf("Voce nao atende ao criterio renda\n");
    } 
} else {
    printf("Voce nao atende ao criterio idade!\n");
}

}