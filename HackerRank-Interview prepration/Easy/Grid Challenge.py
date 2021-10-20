def gridChallenge(arr):
    for j in range(len(arr[0])):
        for i in range(1,len(arr)):
            if arr[i][j]<arr[i-1][j]:
                return "NO"
    return "YES"
for _ in range(int(input())):
    arr = [sorted(input()) for i in range(int(input()))]
    print(gridChallenge(arr))