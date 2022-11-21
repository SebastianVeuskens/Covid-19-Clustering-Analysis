def elabora(a,b,c,):
    a = []
    for k in range(0, len(a)):
        if k % 2 != 0:
            b.append([k])
        if k % 2 == 0 and a[k]>0:
            c.append(a[k])

    r = False
    for k in range(0, len(a), 2):
        if a [k]<0:
            r = True
    return r

#fp = open("numeri.txt")
#x = []
#for v in fp:
    #a =(int(v) for v in fp)
    #x.append(v)

#fp.close()

x = [3, 2, 5, 6, 7, 8, 8, 8, 9, 9, 2,0 ,765,43 ,2 ,-7,-3,-2,-1]
y = []
z = []

r = elabora(x,y,z)

n = min(len(y), len(z)) -1
m = 0
for k in range (n+1):
    m += (abs(y[k])+ abs(z[k]))


print(m)
print(y)
print(z)