#include <stdio.h>
int paradox(int n, int x, int y, int z, int q) {
		if (n==1||n==2) {
			z = 1;
			return z;}
		z = x + y;
		q++;
		if(q==n) {
			return z;}
		x = y + z;
		q++;
		if(q==n) {
			z = x;
			return z;}
		y = z + x;
		q++;
		if(q==n) {
			z = y;
			return z;}
		return paradox(n,x,y,z,q);
	}	
int main() {

	int n;
	int x = 1;
	int y = 1;
	int z;
	int q=2;
	
	printf("Enter a number:");
	scanf("%d", &n);
	z = paradox(n, x, y, z, q);
	printf("\n%d\n", z);
return 0;
}
