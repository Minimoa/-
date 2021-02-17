## 신장 트리

하나의 그래프가 있을때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프 



## 크루스칼 알고리즘

최소한의 비용으로 신장 트리를 찾아야 할 때

ex) N개의 도시가 존재하는 상황에서 두 도시 사이에 도로를 놓아 전체 도시가 서로 연결될 수 있도록 도로를 설치하는 경우 

크루스칼 알고리즘을 사용하며 가장 적은 비용으로 모든 노드를 연결할 수 있으며 `그리디 알고리즘`으로 분류된다.모든 간선에 대하여 정렬을 수행한 뒤에 가장 거리가 짧은 간선부터 집합에 포함시키면 됨 (이때 사이클 발생시키는 간선이면 x)



1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.

2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.

   1. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.

   2. 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다. 

      (각각의 루트 노드가 이미 집합에 포함되어 있는 경우)

3. 모든 간선에 대하여 2번의 과정을 반복한다.   

   

```python
# 특정 원소가 속한 집합 찾기
def find_parent(parent,x):
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a<b:
    parent[b] = a
  else:
    parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력 받기
v,e = map(int,input().split())
parent = [i for i in range(v+1)] # 부모 테이블 상에서 부모를 자기 자신으로 초기화 

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

#모든 간선에 대한 정보를 입력받기 
for _ in range(e):
  a,b,cost = map(int,input().split())
  #비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
  edges.append((cost,a,b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인
for edge in edges:
  cost,a,b = edge
  #사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent,a) != find_parent(parent,b):
    union_parent(parent,a,b)
    result += cost

print(result)

```



간선의 개수가 E개일 때, O(ElogE)의 시간 복잡도를 가진다. E개의 데이터를 정렬하는 시간 복잡도는 O(ElogE)인데 제일 오래 걸리기 때문이다. 
