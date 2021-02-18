## 위상 정렬

방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것 

1. 진입 차수가 0인 노드를 큐에 넣는다
2. 큐가 빌 때까지 다음의 과정을 반복한다.
   1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
   2. 새롭게 진입 차수가 0이된 노드를 큐에 넣는다. 

큐가 모든 원소를 방문하기 전에(큐에서 원소가 V번 추출되기 전에) 큐가 비어버리면 사이클이 발생한 것 

```python
from collections import deque

#노드의 개수와 간선의 개수를 입력받기
v,e = map(int,input().split())
#모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0]*(v+1)
#각 노드에 연결된 간선 정보를 담기 위한 연결리스트 초기화
graph = [[] for _ in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
  a,b = map(int, input().split())
  graph[a].append(b) 
  indegree[b] += 1

#위상 정렬 함수
def topology_sort():
  result = []
  q = deque()

  # 진입 차수가 0인 노드를 큐에 삽입
  for i in range(1,v+1):
    if indegree[i] == 0:
      q.append(i)
  
  # 큐가 빌 때까지 반복
  while q:
    #큐에서 원소 꺼내기
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
      indegree[i]  -= 1
      if indegree[i] == 0:
        q.append(i)


  for i in result:
    print(i,end= ' ')

topology_sort()
```



차례대로 모든 노드를 확인하면서, 해당 노드에서 출발하는 간선을 차례대로 제거해야하기 때문에 모든 노드와 간선을 확인 하는 것과 같으므로 O(V+E)의 시간이 소요된다. 

