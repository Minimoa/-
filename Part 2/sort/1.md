## 처음

```python
n = int(input())

array = [int(input()) for _ in range(n)]
array.sort()

if n == 1:
  print(0)
else:
  total = [array[0]+array[1]]

  for i in range(2,len(array)):
    total.append(total[i-2]+array[i])

  print(sum(total))

```

반례 `4 3 4 5 6`

언뜻보면 맞는 것 같지만 선형으로만 비교하기 때문에 항상 가장 작은 크기의 카드를 합친다는 보장이 없다. 

## 나중

```python
import heapq
n = int(input())
heap = []
for i in range(n):
  data = int(input())
  heapq.heappush(heap,data)

result = 0

while len(heap) != 1:
  one = heapq.heappop(heap)
  two = heapq.heappop(heap)

  sum_value = one + two
  result += sum_value
  heapq.heappush(heap,sum_value)

print(result)
```

힙큐를 사용해 항상 작은 값들끼리 합치도록 한다. 
