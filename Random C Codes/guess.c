#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
	srand(time(NULL));
	int num = rand() % 10;
	num++;
	int userInput;
	do {
	printf("Enter a number:");
	scanf("%d", &userInput);
        }
	while(userInput != num);
	printf("You Guessed It!\n");
	return 0;
}
