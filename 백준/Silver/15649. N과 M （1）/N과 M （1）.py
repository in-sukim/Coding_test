import sys

n,m = map(int, sys.stdin.readline().split())
result = []
def back():
  if len(result) == m:
    print(' '.join(map(str, result)))
  for i in range(1,n+1):
    if i not in result:
      result.append(i)
      back()
      result.pop()
back()