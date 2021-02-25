import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n,m,start = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1) 

for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))

def dijkstra():
  q = [] 
  distance[start] = 0
  heapq.heappush(q,(0,start))

  while q:
    dist,cur = heapq.heappop(q)

    if distance[cur] < dist:
      continue 
    for i in graph[cur]: 
      cost = distance[cur]+i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost

      heapq.heappush(q,(cost,i[0])) 
dijkstra()


total_cost = 0
cnt = -1

for i in distance:
  if i != INF:
    total_cost = max(total_cost,i)
    cnt += 1

print(cnt,total_cost)
