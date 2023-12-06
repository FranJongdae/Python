#include <stdio.h>
int main() {
    float dist, cmedio, pcombustivel, cviagem;

    printf("Informe a distancia da viagem(em Km): ");
    scanf("%f", &dist);

    printf("Informe o consumo medio do automovel(em litros por Km): ");
    scanf("%f", &cmedio);

    printf("Informe o preco do combustivel: ");
    scanf("%f", &pcombustivel);

    cviagem=(dist/cmedio)*pcombustivel;
    printf("O custo estimado da viagem e: %.2f euros\n", cviagem);
 return 0;
}