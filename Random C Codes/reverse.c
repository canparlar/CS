#include <stdio.h>
#include <string.h>

int main () {
	char s1[50];
	int index;
	int index2;
	fgets(s1, sizeof(s1), stdin);
	s1[strlen(s1)-1] = '\0';
	index2 = strlen(s1)-1;
	char s2[index2+1];
	for(index = 0; index < strlen(s1); index++) {
		
		s2[index2] = s1[index];
		index2--;
			
	}
	printf("%s", s2);
	return 0;
}


	
