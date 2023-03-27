def isSquare(mychain):
    clen = len(mychain)
    if (clen % 2 != 0):
        return "NO"
    a,b = mychain[:int(clen/2)], mychain[int(clen/2):]
    if (a == b):
        return "YES"
    return "NO"
n = int(input())
for x in range(0,n):
    chain = input()
    print(isSquare(chain))