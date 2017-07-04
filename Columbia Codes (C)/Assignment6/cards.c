/* Can Parlar - Prints out 5 random cards */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

enum suits {HEARTS = 1, SPADES = 2, DIAMONDS = 3, CLUBS = 4};

typedef struct cards {

	char cards[6];
	int number;
	char suits[10];
} crd;
crd c1, c2, c3, c4, c5, c6;

int drawCard() {

	int num = rand() % 13;
	num ++; num++;
	
	int num2 = rand() % 4;
	num2 ++;
printf("%d\n", num);
if (num == 11) {
strcpy(c6.cards, "Ace");
c6.number = 0;}
if (num == 12) {
strcpy(c6.cards, "King");
c6.number = 0;}
if (num == 13) {
strcpy(c6.cards, "Queen");
c6.number = 0;}
if (num == 14) {
strcpy(c6.cards, "Jack");
c6.number = 0;}
if (num < 11) {
strcpy(c6.cards, "");
c6.number = num;}
if (num2 == HEARTS) {
strcpy(c6.suits, "Hearts");}
if (num2 == SPADES) {
strcpy(c6.suits, "Spades");}
if (num2 == DIAMONDS) {
strcpy(c6.suits, "Diamonds");}
if (num2 == CLUBS) {
strcpy(c6.suits, "Clubs");}
}

int getSuit() {
printf("Drawn Cards:\n%s%d of %s\n", c1.cards, c1.number, c1.suits);
printf("%s%d of %s\n", c2.cards, c2.number, c2.suits);
printf("%s%d of %s\n", c3.cards, c3.number, c3.suits);
printf("%s%d of %s\n", c4.cards, c4.number, c4.suits);
printf("%s%d of %s\n", c5.cards, c5.number, c5.suits);
}

int main() {
	srand(time(NULL));

	drawCard();
	c1 = c6;
	drawCard();
	c2 = c6;
	drawCard();
	c3 = c6;
	drawCard();
	c4 = c6;
	drawCard();
	c5 = c6;
	getSuit();
	
	
	return 0; 
}
