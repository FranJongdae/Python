#include <stdio.h>
#include <stdlib.h>
#include <math.h>
main()
{
    float x1,y1,x2,y2;
    float distancia;
    printf("\nDigite o valor de x1: ");
    scanf("%f",&x1);
    printf("\nDigite o valor de y1: ");
    scanf("%f",&y1);
    printf("\nDigite o valor de x2: ");
    scanf("%f",&x2);
    printf("\nDigite o valor de y2: ");
    scanf("%f",&y2);
    distancia=sqrt(pow((x2-x1),2)+pow((y2-y1),2));
    printf("\nA distancia entre os pontos p1 e p2 é %.2f\n",distancia);
    }