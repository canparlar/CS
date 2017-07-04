import string
import sys

intab   = 'abcdefghijklmnopqrstuvwxyz'
outtab  = 'zyxwvutsrqponmlkjihgfedcba'

tab = string.maketrans(intab, outtab)
s = raw_input('Type some text: ').lower()
print s.translate(tab)
