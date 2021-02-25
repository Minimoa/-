# 2개의 최소 신장 트리를 만들기 위해서 
# 크루스칼 알고리즘으로 신장 트리를 만든 다음 비용이 가장 큰 간선을 하나 제거한다

n,m = map(int,input().split())
graph = []
parent = [i for i in range(n+1)]

for _ in range(m):
  a,b,c = map(int,input().split())
  graph.append((c,a,b))

def find_parent(x):
  if parent[x] != x:
    parent[x] = find_parent(parent[x])
  return parent[x]

def union_parent(a,b):
  a = find_parent(a)
  b = find_parent(b)
  if a<b:
    parent[b] = a
  else:
    parent[a] = b


graph.sort()
def kruskal():
  last = 0
  result = 0
  for i in graph:
    c,a,b = i
    if find_parent(a) == find_parent(b):
      continue
    else:  
      union_parent(a,b)
      result += c
      last = c
  
  print(result-last)
  

kruskal()
