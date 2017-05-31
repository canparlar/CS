#include <stdio.h>
int main () {
int x,y,z;
scanf("%d %d %d", &x,&y,&z);
if((x>=y && y>=z)||(z>=y&&y>=x)) {
  printf("in order");
}
else {
  printf("not in order");
}
return 0;
}
