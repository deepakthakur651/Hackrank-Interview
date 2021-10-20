def luckBalance(k, contests):
    important, optional = [], 0
    for x,y in contests:
        if y: 
            important.append(x)
        else: 
            optional+=x
    if k<len(important):
        s = sorted(important)
        i = len(s)-k
        return optional+sum(s[i:])-sum(s[:i])
    return optional+sum(important)

n,k = map(int,input().split())
contests = [list(map(int,input().split())) for _ in range(n)]
print(luckBalance(k, contests))