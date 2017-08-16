a,b = input().split()
a,b = int(a),int(b)
i = 2
s = 0
while a%2==0 and a!=b:
    if a%i == 0:
        a = a/i
        s+=1
        print (a)
    else:
        break
    if a == b:
        print('MUMKUN')
        print(s)
if a != b:
    print('MUMKUN DEGIL')
