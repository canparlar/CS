#include <stdio.h>
#include <stdlib.h>
int main () {
	int x1, y1, x2, y2;
	int c;
	int subt, xsub, ysub;
	scanf ("%d %d", &x1, &y1);
	scanf ("%d %d", &x2, &y2);
	scanf("%d", &c);
	xsub = abs(x2 - x1); 
	ysub = abs(y2 - y1);
	subt = ysub + xsub;

	if (c==subt||(c>subt && c%2==subt%2)) {
		printf("Y");
	}
else{
		printf("N");
}

	return 0 ;}
