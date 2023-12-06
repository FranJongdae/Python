#include <stdio.h>
#include <math.h>

int main() {
    char nome[50];
    float nota1, nota2, nota3, media;

    printf("Digite o nome do aluno: ");
    scanf("%s", nome);

    printf("Digite a primeira nota: ");
    scanf("%f", &nota1);

    printf("Digite a segunda nota: ");
    scanf("%f", &nota2);

    printf("Digite a terceira nota: ");
    scanf("%f", &nota3);

    media = (nota1+nota2+nota3) / 3;
    media = roundf(media * 10) / 10;

    printf("A media de %s e: %.1f\n", nome, media);

 return 0;
}