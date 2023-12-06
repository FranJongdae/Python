#include <stdio.h>

int main() {
    float A, B, C;

    printf("Digite o valor do lado (A): ");
    scanf("%f", &A);
    printf("Digite o valor do lado (B): ");
    scanf("%f", &B);
    printf("Digite o valor do lado (C): ");
    scanf("%f", &C);

    if ((A + B > C) && (A + C > B) && (B + C > A)) {
        if (A == B && B == C) {
            printf("\nOs lados A, B e C formam um triangulo equilatero.\n");
        } else if (A == B || A == C || B == C) {
            printf("\nOs lados A, B e C formam um triangulo isosceles.\n");
        } else {
            printf("\nOs lados A, B e C formam um triangulo escaleno.\n");
        }
    } else {
        printf("\nOs 3 lados nao formam um triangulo.\n");
    }

    return 0;
}
