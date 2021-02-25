## 선택 정렬

### 매번 가장 작은 것을 선택한다.

가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복한다

```
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
  min_index = i
  for j in range(i+1,len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i],array[min_index] = array[min_index], array[i]
  
```

O(N^2)으로 비효율적

가장 작은 원소 찾는 방법은 기억해두기

## 삽입 정렬

### 각 데이터를 적절한 위치에 삽입한다

정렬되어 있는 데이터 리스트에서 적절한 위치를 찾은 후에 그 위치에 삽입한다. 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다.

-> 두 번째 데이터부터 시작

```
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
  for j in range(i,0,-1): #i번째부터 앞으로 이동한다
    if array[j] < array[j-1]:#한칸씩 왼쪽으로 이동한다
      array[j], array[j-1] = array[j], array[j-1] 
    else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춘다
      break
```

최악 O(N^2)

최선 O(N)

거의 정렬되어 있는 상태일때는 매우 빠름

## 퀵 정렬

### 기준 데이터를 설정하고 좌우 위치를 바꾼다

기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작한다.

교환을 위한 기준 = `피벗`

#### 호어분할

#### 1. 분할

- 리스트에서 첫 번째 데이터를 피벗으로 정한다.

  왼쪽에서부터 피벗보다 큰 데이터를 찾고 오른쪽에서부터 피벗보다 작은 데이터를 찾아서 교환한다

- 왼쪽과 오른쪽에서 찾는 값이 엇갈릴 경우에는 `작은 데이터`와 `피벗`의 위치를 서로 변경한다. 

- 피벗의 왼쪽 데이터는 피벗보다 작고 오른쪽은 피벗보다 큰 상태가 된다.  > 분할 , 파티션

### 2.

​	동일한 방법으로 피벗의 왼쪽 데이터들을 정렬한다. 

#### 3. 

​	동일한 방법으로 피벗의 오른쪽 데이터들을 정렬한다. 



재귀로 구현하면 간결함. 현재 리스트의 원소가 1개라면 이미 정렬되어 있다고 간주하며 분할이 불가능함

```python
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
  if start >= end:
    return
  pivot = start
  left = start+1
  right = end
  while left <= right:
    # 피벗보다 큰 데이터를 찾을 때까지 반복
    while left<=end and array[left] <= array[pivot]:
      left += 1
    # 피벗보다 작은 데이터를 찾을 때까지 반복
    while right> start and array[right] >= array[pivot]:
      right -= 1
    if left > right: #엇갈렸다면 작은 데이터와 피벗을 교체
      array[right], array[pivot] = array[pivot], array[right]
    else:# 엇갈리지 않았다면 큰 데이터와 작은 데이터를 교체 
      array[left], array[right] = array[right], array[left]

  #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행  
  quick_sort(array,start,right-1)
  quick_sort(array,right+1,end)



quick_sort(array,0,len(array)-1)
print(array)
```

파이써닉한 방법 시간은 조금 비효율적이지만 직관적임

```python
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
  if len(array) <= 1:
    return array
  
  pivot = array[0] # 피벗을 첫 번째 원소 
  tail = array[1:] # 피벗을 제외한 리스트

  left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
  right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```



최선 O(nlogn)

최악 O(n^2) 이미 정렬되어 있는 경우에 비효율적임



정렬  라이브러리의 경우 퀵 소트 기반이지만 최악의 경우에도 O(nlogn)이 나오도록 보장됨



## 계수 정렬

### 특정 조건이 부합할 때만 사용할 수 있지만 매우 빠르다

일반적으로 별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담는다

큰 데이터와 작은 데이터의 차이가 1,000,000을 넘지 않을때 효과적으로 사용할 수 있다. 

- 가장 큰 데이터와 가장 작은 데이터의 범위가 모두 담길 수 있도록 하나의 리스트를 생성한다.
- 처음에는 리스트의 모든 데이터가 0이 되도록 초기화한다. 
- 그 다음 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가시키면 계수 정렬이 완료된다.
- 결과적으로 리스트에는 각 데이터가 몇 번 등장했는지 그 횟수가 기록되기 때문에 횟수만큼 차례로 출력하면 됨

```python
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0]*(max(array)+1)

for i in range(len(array)):
  count[array[i]] += 1 #각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end = ' ')

```

데이터가 양의 정수인 상황에서 데이터 개수를 N, 데이터 중 최대값의 크기를 K라고 할때 

O(N+K)

데이터의 크기가 한정되어 있고, 동일한 값을 가지는 데이터가 여러개 등장할때 적합하다.



## 코딩 테스트에서 정렬 알고리즘이 사용되는 경우

1. 정렬 라이브러리로 풀 수 있는 문제

2. 정렬 알고리즘의 원리에 대해서 물어보는 문제

3. 더 빠른 정렬이 필요한 문제 





python sort 함수는 lambda를 이용해 키를 지정할 수 있다 .

```python
    numbers.sort(key= lambda x: x*3, reverse = True)
```

