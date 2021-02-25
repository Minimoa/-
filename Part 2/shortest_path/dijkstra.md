## 다익스트라 최단 경로 알고리즘 (Dijkstra)
`한 지점에서 다른 특정 지점까지의 최단 경로를 구해야하는 경우`  
여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘. `가장 비용이 적은 노드`를 선택해서 임의의 과정을 반복하기 때문에 `그리디` 알고리즘으로 분류된다.

```
1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
5. 위 과정에서 3,4번을 반복한다.	
```

`각 노드에 대한 현재까지의 최단 거리` 정보를 리스트에 저장하며 계속 갱신한다. 매번 현재 처리하고 있는 노드를 기준으로 주변 간선을 확인함



### 간단한 다익스트라 알고리즘

```python
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드의 개수, 간선의 개수
n,m = map(int,input().split())
start = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
  a,b,c = map(int,input().split())
  #a에서 b로 가는 비용이 c
  graph[a].append((b,c))

#방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1,n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  #시작 노드 초기화
  distance[start] = 0
  visited[start] = True

  for j in graph[start]:
    distance[j[0]] = j[1]
  #시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
  for i in range(n-1):
    # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
    now = get_smallest_node()
    visited[now]= True
    # 현재 노드와 연결된 다른 노드를 확인
    for j in graph[now]:
      cost = distance[now] + j[1]
      #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[j[0]]:
        distance[j[0]] = cost



#다익스트라 알고리즘 수행
dijkstra(start)


#모든 노드로 가기 위한 최단 거리 출력
for i in range(1,n+1):
  #도달할 수 없는 경우, 무한이라고 출력
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])
```

`O(V^2)` 으로 5000개 이하면 괜찮지만 10,000개 이상일때는 해결할 수 없음 



### 개선된 다익스트라 알고리즘 



```python
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))

def dijkstra():
  distance[start] = 0
  q = []
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

for i in range(1,n+1):
  if distance[i] == INF:
    print("INFINITE")
  else:
    print(distance[i])


```

우선순위큐를 사용하여 시간복잡도가 `O(ElogV)` 로 개선됨

E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과 유사하기 때문에 `O(ElogE)`이고 중복 간선을 포함하지 않는 경우 `E`는 항상` V^2`보다 작다. 모든 노드끼리 다 연결되어 있다고 했을때 간선의 갯수는 약` V^2`개이므로 항상 `V^2` 이하이고 `logE <= logV^2 ` , `O(logV^2) = O(2logV) = O(logV)` 이므로 전체 시간 복잡도는 `O(ElogV)`
