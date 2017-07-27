import math

disks = [1]
rods = ['A', 'B', 'C']
initial = 1
usr = input()
arry = [0] * c

for n in range(1, usr):
    disks.extend(a)
    disks.insert((2**n)-1, initial+1)
    initial+=1

#print(disks)

if usr%2 == 0:
    for x in range(0,len(disks)):
        if disks[x]%2==0:

            if arry[disks[x]]+2==3:
                #buraya eger 3 u asarsa geri indiricek birsey lazim
            print disks[x],"goes from",rods[arry[disks[x]]+1] ,"to",rods[arry[disks[x]]+2]
        else:
            #eger disk numarasi tek ise tam tersini yapicak
            print disks[x],"goes from",rods[] ,"to",rods[]
else:
#ayni kod sadece siralar farkli
