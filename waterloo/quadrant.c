#include <stdio.h>

int main() {
	
	int x;
	int y;
	int q;
	scanf("%d", &x);
	scanf("%d", &y);

	if (x>0 && y>0){
	q = 1;}

	if (x<0 && y<0){
	q = 3;}

	if(x>0 && y<0){
	q = 4;}

	if (x<0 && y>0){
	q = 2;}

	printf("%d", q);
	return 0;
}
