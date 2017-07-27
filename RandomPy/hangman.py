print('Welcome to HANGMAN!'.center(100,'='))
inp = input('Word:')
for i in range(0,15):
    print ('\n')

word = []
for i in range (0,len(inp)):
    word.append('_')

while (1):

    print (' '.join(word))

    guess = input('\nGuess Letter:')
    if guess == 'q':
        break
    if guess in inp == 1:
        word[inp.index(guess)] = guess
        print ('yey')
