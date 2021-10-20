def maximumPerimeterTriangle(a):
    for i in range(0,len(a)-2):
        if a[i]<a[i+1]+a[i+2]:
            return [a[i+2],a[i+1],a[i]]
    return [-1]
input()
a = sorted(map(int,input().split()), reverse=True)
print(*maximumPerimeterTriangle(a))