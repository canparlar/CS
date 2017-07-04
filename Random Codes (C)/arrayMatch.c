#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main () {
srand(time(NULL));
int arr [15];
int index;
int number;
int same = 0;
for(index = 0; index < 16; index++) {
	int num = (rand() % 10)+1;
	arr[index] = num;
		printf("%d\n", arr[index]);
}

for(number = 1; number < 11; number++) {
	for(index = 0; index < 15; index++) {
		if (arr[index] == number) {
			same++;
		}}
		if (same >= 3) {
			printf("There are %d %d's\n", same, number);
			same = 0;
		}
		else {
			same = 0;
		}

	
}


	return 0;
}
