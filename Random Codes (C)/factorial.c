#include <stdio.h>

int paradox(int x, int y) {
	x = x*y;
	y--;
	if (y==1) {
		return x;}
	else {
	return paradox(x,y);
	}}



int main () {
int x;
	printf("Enter a number:");
	scanf("%d", &x);
	int y = x-1;
	x = paradox(x, y);
	printf("%d\n", x);
	return 0;
}
