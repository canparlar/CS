import math

a = [1]
s = ['A', 'B', 'C']
b = 1
c = input()
y = 0

for n in range(1, c):
    a.extend(a)
    a.insert((2**n)-1, b+1)
    b+=1

#print(a)

if c%2 == 0:
    for x in range(0,len(a)):
        if a[x]%2==0:
            if y+1==3:
                y=0
                print a[x],"goes from",s[y] ,"to",s[y+1]
else:
    for x in range(0,len(a)):
        if a[x]%2==0:
            print a[x],"goes from",s[y] ,"to",s[z]
