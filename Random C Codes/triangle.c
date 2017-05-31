#include <stdio.h>
#include <math.h>

int triangle (int x, int y) {
	float z;
	x = x*x;
	y = y*y;
	z = x+y;
	z = sqrt(z);
	return z;
}

int main () {
	int a;
	int b;
	float c;
	printf("Enter a:");
	scanf("%d", &a);
	printf("Enter b:");
	scanf("%d", &b);
	c = triangle (a, b);
	printf("%f", c);

	return 0;
}

