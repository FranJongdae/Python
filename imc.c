#include <stdio.h>
int main() {
    char nome[50];
    int idade;
    float peso, altura, imc;

    printf("Digite o seu nome: ");
    scanf("%s", nome);

    printf("Digite a sua idade: ");
    scanf("%d", &idade);

    printf("Digite o seu peso: ");
    scanf("%f", &peso);

    printf("Digite a sua altura (em cm): ");
    scanf("%f", &altura);

    altura = altura / 100.0;
    imc = (peso / (altura * altura));
    printf("\nO meu nome e %s, tenho %d anos, peso %.2f Kg, meco %.2f metros. O meu IMC e %.2f.\n", nome, idade, peso, altura, imc);

 return 0;
}
