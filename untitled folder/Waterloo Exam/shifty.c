#include <stdio.h>

int main () {

	int n;
	int k;
	int i;
	scanf("%d", &n);
	scanf("%d", &k);
	int sum = n;

	for (i = 0; i<k; i++) {
	n = n * 10;
	sum = sum + n;}

	printf("%d", sum);
	return 0;
}
