#include <stdio.h>

int main () {

	int minute;
	int sonuc = 0;
	int iq;
	int d1,d2,d3,d4;
	int x = 0;
	int min = 0;
	int hours[12] = {12,1,2,3,4,5,6,7,8,9,10,11}; 
	
	scanf("%d", &minute);

	for (iq = 0; iq<minute; iq++) {	

		min++;

		if (min == 60) {
			x++;	
			min = 0;}

		if (x == 12) {
		x = 0; }

		d3 = min/10;
                d4 = min %10;
		
		if (0<x&&x<10) {
		d1 = hours[x];
			if(d4-d3==d3-d1){
			sonuc++;}}
		
		else {
		d1 = hours[x] / 10;
		d2 = hours[x] % 10;
		if((d4-d3)==(d3-d2)&&(d3-d2)==(d2-d1)){
		sonuc++;}}
printf("%d",sonuc);
	return 0;
}
