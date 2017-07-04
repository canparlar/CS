# Assignment 6
## Objectives

To gain a solid understanding of structures and enums.

### Part 1
1. Write a program `cards.c` that implements a deck of cards.  Implement the suits as an enum, and the cards as a struct containing the value and suit.  Implement a function `drawCard()` to generate a random card and `getSuit()` to print out the the suit properly.  In main, draw and print out 5 cards in the following format:

```
Drawn Cards:
	5 of hearts
	10 of diamonds
	Queen of spades
	2 of clubs
	Ace of hearts
```

2.  Write a program `company.c` that implements an employee structure containing a name, position, and a salary.  Create an array of 5 employees in your main function, each with a different name and salary.  Write a function output() that takes an employee array and prints out the array of employees in the following format:
```	
Name		  	Position	  	Salary
-------------------------------------------- 
John Smith		Manager	    	$3000.25 
Angela Lee		Accountant		$2270.00

```

### Part 2

In a text file `assignment6.txt`, answer the following questions:

1.  Is there anything wrong with this code? If so, what is it and how would you fix it?
  
``` C
#include <stdio.h> 
int main() {
  int num, n;
  int arr[num];
  printf(“Enter the size of an array”); 
  scanf(“%d”, &num);
  for (n=0; n<num; n++) {
    arr[n] = 0;
  }
}

```

2. In your own words, what is a segmentation fault? Give an example. 

3. Explain the difference between an enum and a struct.

4. Can you include an enum within a struct? If so, how would you go about this?

### Submission Guidelines
Please include your name and a description in a comment at the top of your code files. Please also include your name at the top of your assignment6.txt file. Make sure to include comments for each file and function. 

All files must be submitted via GitHub by 10:10am 8/1. 
