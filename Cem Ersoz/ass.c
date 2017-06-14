#include <stdio.h>
#include <string.h>

char sfirst[60];
char ssecond[60];

int split (char sinput[40], char ssplitter[40]) {

  char *search;
  search = strstr(sinput, ssplitter);

  if (search != NULL) {

      strncpy(sfirst, sinput, (search-sinput));
      strncpy(ssecond, sinput+(search-sinput)+strlen(ssplitter)+1, strlen(sinput));

      return 1;
  }

  else {
      printf("No Splitter in Input\n");
      return 0;
  }
}

int list () {

    char *ptr;

    do {
      ptr = strtok (sfirst," ,.");
      printf ("%s\n",ptr);
    } while (ptr != NULL)

    return 1;
}

int translate () {



}

 int main () {

	 char sinput[100];
   char ssplitter[100];

	 printf("Input:");
	 fgets(sinput, sizeof(sinput), stdin);
	 sinput[strlen(sinput)-1] = '\0';

   printf("Splitter:");
   fgets(ssplitter, sizeof(ssplitter), stdin);
   ssplitter[strlen(ssplitter)-1] = '\0';

	 split(sinput, ssplitter);

   list();

   translate();

   printf("First:%s\nSecond:%s\n",sfirst,ssecond);

	 return 0;
}
