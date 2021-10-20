import sys
import math

input = sys.stdin


N = int(input.readline())
stars = [tuple(map(int, input.readline().split())) for _ in xrange(N)]
W = sum(w for _, _, w in stars)

angles = []
for i in xrange(N - 1):
  for j in xrange(i + 1, N):
    x1, y1, _ = stars[i]
    x2, y2, _ = stars[j]
    angles.append(math.atan2(y1 - y2, x2 - x1))

def rotate(star, a):
  x, y, w = star

  xr = x * math.cos(-a) - y * math.sin(-a)
  yr = x * math.sin(-a) + y * math.cos(-a)
  return xr, yr, w

def solve(a):
  rotated = map(lambda s: rotate(s, a), stars)
  rotated.sort(lambda p, q: cmp(p[1], q[1]))
  w = 0
  ret = 0
  for i in xrange(N):
    w += rotated[i][2]
    m = min(w, W - w)
    ret = max(ret, m)
  return ret

sol = 0
for a in angles:
  sol = max(sol, solve(a))
print sol
