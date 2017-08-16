n = int(input())
l = []
d = 200
for i in range(n):
    l.append(int(input()))
for i in range(len(l)):
    a = sum(l[:i])
    b = sum(l[i:])
    c = abs(a-b)
    if c < d:
        d = c
        num = i

print (num)
