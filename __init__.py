n = int(raw_input())

for i in range (1,n+1):
    for j in range (1,i+1):
        print "*",
    print

for i in range (1,n+1):
    for j in range (n,i-1,-1):
        print "*",
    print

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print i,
    print

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print j,
    print


for i in range(1, n + 1):
    for j in range(n, i - 1, -1):
        print i,
    print

for i in range(1, n + 1):
    for j in range(n, i - 1, -1):
        print j,
    print

k=1;
for i in range (1,n+1):
    for j in range (1,i+1):
        print k,
        k+=1
    print

for i in range(n,0,-1):
    for j in range(1,i+1):
        print i,
    print