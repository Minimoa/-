## 순차탐색

리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법

O(N)



## 이진 탐색 : 반으로 쪼개면서 탐색하기

시작점, 끝점, 중간점을 놓고 중간점 위치에 있는 데이터를 반복적으로 비교

### 재귀로 구현

```python
def binary_search(array,target,start,end):
  if start>end:
    return None
  mid = (start + end) //2 

  if array[mid] == target:
    return mid
  
  # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
  elif array[mid] > target:
    return binary_search(array,target,start,mid-1)
  
  # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
  else:
    return binary_search(array,target,mid+1,end)

n,target = list(map(int,input().split()))
array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)
if result == None:
  print("x")
else:
  print(result+1)

```

### 반복문 구현 

```python
def binary_search(array,target,start,end):
  while start<=end:
    mid = (start+end)//2
    if array[mid] == target:
      return mid
    elif array[mid] < target:
      start = mid+1
    else:
      end = mid-1
  return None

n,target = map(int,input().split())
array = list(map(int,input().split()))
result = binary_search(array,target,0,n-1)
if result == None:
  print("x")
else:
  print(result+1)

```

데이터 개수나 값이 1000만 단위 이상으로 넘어가면 O(longN)의 속도를 내야하는 알고리즘을 생각해야 풀 수 있는 경우가 많다. 

이진 탐색도 O(logN)
