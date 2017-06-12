#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    char sntnc[50], word[50];
    puts("\nEnter a sentence");
    gets(sntnc);
    fflush(stdin);
    puts("\nEnter a word");
    gets(word);
    fflush(stdin);

    char *s;

   s = strstr(sntnc, word);      // search for string "hassasin" in buff
   if (s != NULL)                     // if successful then s now points at "hassasin"
   {
       printf("Found string at index = %ld\n", s - sntnc);
   }                                  // index of "hassasin" in buff can be found by pointer subtraction
   else
   {
       printf("String not found\n");  // `strstr` returns NULL if search string not found
   }
}
