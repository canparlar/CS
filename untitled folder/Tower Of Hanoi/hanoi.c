#include <stdio.h>
int sum = 0;
void towerOfHanoi(int n, char fromrod, char torod, char auxrod)
{
  sum++;
    if (n == 1)
    {
        printf("\n Move disk 1 from rod %c to rod %c", fromrod, torod);
        return;
    }
    towerOfHanoi(n-1, fromrod, auxrod, torod);
    printf("\n Move disk %d from rod %c to rod %c", n, fromrod, torod);
    towerOfHanoi(n-1, auxrod, torod, fromrod);
}

int main()
{
    int n;
    scanf("%d",&n);
    towerOfHanoi(n, 'A', 'C', 'B');
    printf("%d",sum);
    return 0;
}
