## 플로이드 워셜 알고리즘 (Floyd-Warshall Algorithm)

모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야하는 경우 

단계마다 `거쳐 가는 노드`를 기준으로 알고리즘을 수행한다. 단계마다 `O(N^2)`의 연산을 통해 `현재 노드를 거쳐가는` 모든 경로를 고려한다. 따라서 총 `O(N^3)`

최단 거리 정보를 2차원 리스트에 저장한다.  `다이나믹 프로그래밍`으로 분류되는데 노드의 개수가 N일때, N번 만큼의 단계를 반복하며 `점화식에 맞게` 2차원 리스트를 갱신하기 때문

각 단계에서 해당 노드를 거쳐가는 모든 경우를 고려해야한다. 

1번 노드에 대해서 확인 할 경우

`A → 1 → B `로 가는 비용을 확인한 후에 최단 거리를 갱신한다.

`A → B `보다 작으면 업데이트 

이때 (A,B)는 현재 확인하고 있는 노드를 제외한 N-1개의 노드 중에서 서로 다른 노드이므로 점화식은 이렇게된다. 
![image](https://user-images.githubusercontent.com/13061461/108040107-40c96f80-7080-11eb-8caf-49b2cbbbc862.png)

N-1 개 중에서 2개를 고르는 순열이기 때문에 _(N-1)P_2 이고 ![img](https://blog.kakaocdn.net/dn/cR3YOt/btqHBTdPGBn/X3nvQO9sWOnvKiaF79HtVK/img.png)이므로

이걸 N번 반복하니까 총 O(N^3)이다.

### 구현

1. n*n 인접 매트릭스를 만들어서 간선 비용을 넣는다. 루프는 0, 연결되지 않은 간선은 무한으로 놓는다.
2. 첫번째 노드부터 해당 노드를 제외하고 두쌍을 선택하는 모든 경우에서 점화식을 적용한다. 



```python
import sys 
input = sys.stdin.readline
INF = int(1e9)

#노드 개수
n = int(input())
#간선 개수
m = int(input())

#2차원 리스트 무한으로 초기화 
graph = [[INF]*(n+1) for _ in range(n+1)]

#루프는 0으로 초기화
for a in range(1,n+1):
  graph[a][a] = 0

#각 간선 정보 입력 받기
for _ in range(m):
  # A에서 B로 가는 비용은 C
  a,b,c = map(int,input().split())
  graph[a][b] = c

#점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

#수행된 결과를 출력
for a in range(1,n+1):
  for b in range(1,n+1):
    if graph[a][b] == INF:
      print("INFINITY",end =" ")
    else:
      print(graph[a][b],end=" ")
  print()
```

