#include<stdio.h>
int main()
{
    char a[30];
    int i=0;
    while( (a[i++]=getchar()) != '\n' && i < 30)
     a[i] = '\0';
     i = 0;
     while(a[i] != '\0')
         printf("%c\n\n",a[i++]);

     return 0;
}
