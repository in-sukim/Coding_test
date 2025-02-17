import sys
sys.setrecursionlimit(10 ** 6)
n,m,r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  u,v = map(int, sys.stdin.readline().split())
  graph[u].append(v)
  graph[v].append(u)

visited = [0] * (n+1)
cnt = 1

def dfs(r):
  global cnt
  visited[r] = cnt
  for node in sorted(graph[r]):
    if not visited[node]:
      cnt += 1
      dfs(node)
dfs(r)
for i in range(1, n+1):
  print(visited[i])