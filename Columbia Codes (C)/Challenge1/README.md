# Challenge Assignment 1
This is an OPTIONAL challenge assignment.  You are not required to do this assignment, and you should not attempt it before you've finished other work for this class.  This assignment is purely for further practice.

## Objectives
Gain further experience through a more challenging assignment in working with arrays and strings in C, and get practice using arrays, strings, and functions.

Required knowledge: variables, conditional statements, loops, arrays, strings, functions

## Part 1
Write a program `minesweeper.c` that takes in dimensions m and n from the user and a probability p, then generates a Minesweeper board of size m x n where each cell has a probability of p to be a mine (probability is a number between 0 and 1).  Each cell that is not a mine contains a number representing how many mines (above, below, left, right, and diagonal) neighbor that "safe" cell.  Print the board, representing each mine as an asterisk (*).

Your program should check for valid input.

Some tips:
	* You may want to store your board as an integer array, with some constant value for the mines (e.g. 99), then convert the integer representation to a * for printing

## Part 2
Write a program `hangman.c` implementing the Hangman game.  Your program should do the following cleanly and efficiently using functions as needed:
* Get a random word from an array of words (the array should have at least 10 words in it).  You may hardcode this array.
* Each turn, display a set of blanks for each letter of the word to guess, the bank of correctly guessed letters, and the bank of incorrectly guessed letters.
* Ask the user if they want to guess a letter or the entire word.
* Prompt the user for a letter (or the entire word, as appropriate).
* Change the blanks to letters as they are guessed correctly
* Subtract 1 from allowed incorrect guesses and draw the hangman figure as appropriate (you may make your hangman ascii art as simple/complex as you like, but the allowed incorrect guesses should reflect this number)
* Ensure that the user cannot guess a letter twice or guess a non-alphabetic character

Some tips:
* It may be helpful to have all letters be uppercase or lowercase, and convert user input as appropriate
* You should definitely use functions for this
* Some useful library functions:
	* `c = toupper(c)` will convert c to uppercase.  It is in the ctype.h library, so you will need to include that if you want to use this.  Similarly, c = tolower(c) will convert the character stored in c to lowercase
	* `isalpha(c)` returns a 0 if the value stored in variable c is not a letter, and a non-zero number otherwise.  This function is also in the ctype.h library.
	

### Submission Guidelines
This is an optional assignment, so there is no due date.  Submit it just as you would any other assignment.

As these are larger coding exercises, you may want to add/commit/push often so that you can roll back any accidental changes you make.
