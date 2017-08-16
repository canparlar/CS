# For given n number of integers, calculates how many
# triangles can be formed by using those numbers as edges.
n = input()
l = input().split()
s = []
result = 0

for a in l:
    for b in l:
        for c in l:
            a,b,c = int(a),int(b), int(c)
            if a != b and c !=b and a!=c:
                if abs(a+b)>c and abs(a-b)<c:
                    y = [a,b,c]
                    y.sort()
                    s.append(y)
for a in s:
    for b in s:
        if a == b:
            s.remove(b)
result = len(s)
print result
