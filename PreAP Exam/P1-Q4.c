#include <stdio.h>
#include <stdlib.h>
int main () {
  int a,b;
scanf("%d", &a);
scanf("%d", &b);
printf("%d\n", a+b);
printf("%d\n", abs(a-b));
printf("%d\n", a*b);
printf("%d\n", (a+b)/2);
if (a>b) {
printf("max:%d\n", a);
printf("min:%d\n", b);}
if (b>a) {
printf("max:%d\n", b);
printf("min:%d\n", a);}

}
