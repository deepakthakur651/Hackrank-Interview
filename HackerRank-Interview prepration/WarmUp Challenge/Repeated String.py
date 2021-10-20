def repeatedString(s, n):
    x,y = divmod(n,len(s))
    return s[:y].count("a")*(x+1) + s[y:].count("a")*x
s = input()
n = int(input())
print(repeatedString(s, n))