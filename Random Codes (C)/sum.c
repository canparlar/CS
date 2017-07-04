#include <stdio.h>

int main() {
	int uInput;
	int sum = 0;
	printf("Enter a natural number:");
	scanf("%d", &uInput);
	for (; uInput>0; uInput--) {	
	sum += uInput;
	}
	printf("%d\n",sum);
}
