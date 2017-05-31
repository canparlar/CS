#ifndef max
#define max(a,b)            (((a) > (b)) ? (a) : (b))
#endif
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main () {
double r,g,b;
scanf("%lf %lf %lf", &r,&g,&b);
double white = max((r/255), max((g/255),(b/255)));
double cyan = (white - (r/255)) / white;
double mag = (white - (g/255)) / white;
double yel = (white - (b/255)) / white;
double black = 1 - white;
printf("%f \n%f \n%f \n%f \n", cyan, mag,yel, black);

}
