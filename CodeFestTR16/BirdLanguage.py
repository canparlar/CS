# Gets a string and converts the string into bird language
# after every vowel o and again the vowel comes
s = str(input())
i = 0
while True:
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
        print (s)
        s = s[:i+1] + 'g' + s[i:]
        i+=2
    i+=1
    if i == len(s):
        break
print (s)
