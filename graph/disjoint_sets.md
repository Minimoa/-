## 서로소 집합

공통 원소가 없는 두 집합, 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조

- union : 합집합 
- find : 특정 원소가 속한 집합 찾기



### 서로소 집합 자료구조(union_find)

트리로 표현함

1. 합집합을 확인해서 서로 연결된 두 노드 A,B를 확인한다

   1. A와 B의 루트노드 a,b를 각각 찾는다

   2. a를 b의 부모 노드로 설정한다. (b가 a를 가리키도록 한다.)

      더 작은 번호가 부모가 되고, 큰 번호가 자식이 된다. 

2. 모든 합집합 연산을 처리할 때까지 1번 과정을 반복한다. 



```python
# 특정 원소가 속한 집합 찾기
def find_parent(parent,x):
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x:
    return find_parent(parent,parent[x])
  return x

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

#union 연산을 각각 수행
for i in range(e):
  a,b = map(int,input().split())
  union_parent(parent,a,b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합 : ', end=' ')
for i in range(1,v+1):
  print(find_parent(parent,i),end=' ')


print()

#부모 테이블 출력 
print('부모 테이블: ',end=' ')
for i in range(1,v+1):
  print(parent[i],end=' ')


```

find 함수가 최대 O(V)으로 union이 M일때, 전체 시간 복잡도는 O(VM)이 되어 비효율적임 



### 경로 압축을 통한 최적화 

find함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 갱신한다

최상단의 부모로 바로 부모 테이블 값을 설정  

```python
# 특정 원소가 속한 집합 찾기
def find_parent(parent,x):
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출한 뒤에 부모 테이블 값을 갱신
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]
```

노드의 개수가 V개이고, 최대 V-1개의 union 연산과 M개의 find 연산이 가능할때 시간복잡도는 O(V+M(1+log_2-m/VV)). 노드의 개수가 1,000개이고 union 및 find 연산이 총 100만 번 수행된다고 할대 대략 1000만 번 가량 연산이 필요함 



### 서로소 집합을 활용한 사이클 판별 

무방향 그래프 내에서 사이클을 판별할 때 사용할 수 있음 (방향 그래프일때는 DFS)

1. 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
   1. 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산을 수행한다.
   2. 루트 노드가 서로 같다면 사이클이 발생한 것이다. 
2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복한다. 

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
cycle = False

#union 연산을 각각 수행
for i in range(e):
  a,b = map(int,input().split())
  # 사이클이 발생한 경우 종료
  if find_parent(parent,a) == find_parent(parent,b):
    cycle = True
    break
  # 사이클이 없으면 합집합 
  union_parent(parent,a,b)


if cycle:
  print("사이클이 발생했습니다.")
else:
  print("사이클이 발생하지 않았습니다.")
```

