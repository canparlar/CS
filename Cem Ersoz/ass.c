//This code splits a string by a splitting word and translates written numbers to numbers.

#include <stdio.h> //@cemersoz included standart library
#include <string.h> //included string library

char sfirst[60]; //first word (number)
char ssecond[60]; //second word (number)

int split (char sinput[40], char ssplitter[40]) {

  char *search; //created a pointer to search
  search = strstr(sinput, ssplitter); //searches for the splitting word

  if (search != NULL) { //if the splitter is present in the sentence

      strncpy(sfirst, sinput, (search-sinput)); //splits the first word to sfirst
      strncpy(ssecond, sinput+(search-sinput)+strlen(ssplitter)+1, strlen(sinput)); //splits the second word to ssecond

      return 1;
  }

  else { //if the splitter is not present in the sentence
      printf("No Splitter in Input\n");
      return 0;
  }
}

int list () { //lists the strings

    char *ptr;

    do {
      ptr = strtok (sfirst," ,.");
      printf ("%s\n",ptr);
    } while (ptr != NULL)

    return 1;
}

int translate () { //translates words to numbers



}

 int main () {

	 char sinput[100]; //input sentence
   char ssplitter[100]; //splitting word

	 printf("Input:");
	 fgets(sinput, sizeof(sinput), stdin); //gets the input sentence
	 sinput[strlen(sinput)-1] = '\0';

   printf("Splitter:");
   fgets(ssplitter, sizeof(ssplitter), stdin); //gets the splitting word
   ssplitter[strlen(ssplitter)-1] = '\0';

	 split(sinput, ssplitter); //splits

   list(); //lists

   translate(); //translates

   printf("First:%s\nSecond:%s\n",sfirst,ssecond);

	 return 0;
}
