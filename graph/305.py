# 위상 정렬하여 각 선수 노드의 값을 누적한다.
# 그래프에 넣을때는 해당 인덱스를 선수로 하는 노드를 이중 배열로 

from collections import deque
import copy

n = int(input())
graph = [[] for _ in range(n+1)] 
indegree = [0]*(n+1)
times = [0]*(n+1)
result = []

for i in range(1,n+1):
  tmp = list(map(int,input().split())) 
  times[i] = tmp[0]
  for j in tmp[1:len(tmp)-1]:
    graph[j].append(i)  
    indegree[i] += 1
 
def topology_sort():
  q = deque()
  result = copy.deepcopy(times)
  for i in indegree[1:]:
    if indegree[i] == 0:
      q.append(i)
  while q:
    cur = q.popleft()
    for i in graph[cur]:
      result[i] = max(result[i],result[cur]+times[i])
      indegree[i]-=1
      if indegree[i] == 0:
        q.append(i) 
  for r in result[1:]:
    print(r)

topology_sort()
