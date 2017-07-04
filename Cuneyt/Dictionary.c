#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (void) {
    char input[80];
    char *key;
    int value;
    typedef union cell_t {
        const char *key;
        int value;
        void *ptr;
    } cell;
    typedef struct pair_t {
        cell A;
        cell B;
    } pair;
    pair *top = NULL;
    pair *p;
    pair *q;
    while (1) {
        printf("Enter command (I/P/Q/R): ");
        int command = getchar();
        int c;
        while ((c = getchar()) != '\n' && c != EOF)
            ;
        switch (command) {
            case 'I':
                printf("Enter key: ");
                if (fgets(input, sizeof input, stdin) == NULL) {
                    return 0;
                }
                input[strlen(input) - 1] = 0;
                key = malloc(strlen(input) + 1);
                strcpy(key, input);
                printf("Enter value: ");
                if (fgets(input, sizeof input, stdin) == NULL) {
                    return 0;
                }
                if (sscanf(input, "%d", &value) != 1) {
                    return 0;
                }
                p = malloc(sizeof (pair));
                p->A.key = key;
                p->B.value = value;
                q = malloc(sizeof (pair));
                q->A.ptr = p;
                q->B.ptr = top;
                top = q;
                break;
            case 'P':
                p = top;
                while (p != NULL) {
                    q = p->A.ptr;
                    printf("%-30s %10d\n", q->A.key, q->B.value);
                    p = p->B.ptr;
                }
                break;
            case 'Q':
                return 0;
            case 'R':
                printf("Enter key: ");
                if (fgets(input, sizeof input, stdin) == NULL) {
                    return 0;
                }
                input[strlen(input) - 1] = 0;
                key = malloc(strlen(input) + 1);
                strcpy(key, input);
                p = top;
                while (p != NULL) {
                    q = p->A.ptr;
                    if (strcmp(key, q->A.key) == 0) {
                        printf("%-30s -> %10d\n", q->A.key, q->B.value);
                        break;
                    }
                    p = p->B.ptr;
                }
                break;
        }
    }
    return 0;
}
