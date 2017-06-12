#include <stdio.h>
#include <string.h>

int palindrome (char sinput[40], char ssplitter[40]) {

  char sfirst[20];
  char ssecond[20];

  char *search;
  search = strstr(sinput, ssplitter);

  if (search != NULL) {
      //printf("Found string at index = %ld\n", search - sinput);

      strncpy(sfirst, sinput, (search-sinput));
      strncpy(ssecond, sinput+(search-sinput)+strlen(ssplitter)+1, strlen(sinput));

      printf("First:%s\nSecond:%s\n",sfirst,ssecond);

      return 0;
  }
  else {
      return 0;
  }
}


 int main () {

	 char sinput[40];
   char ssplitter[40];

	 printf("Input String:");
	 fgets(sinput, sizeof(sinput), stdin);
	 sinput[strlen(sinput)-1] = '\0';

   printf("Splitter:");
   fgets(ssplitter, sizeof(ssplitter), stdin);
   ssplitter[strlen(ssplitter)-1] = '\0';

	 palindrome(sinput, ssplitter);

	 return 0;
}
