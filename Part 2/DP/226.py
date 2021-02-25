# 점화식 
# a[i] : 최소한의 화폐 개수 , k : 화폐의 단위
# a[i-k]를 만들 수 있는 경우 a[i] = min(a[i],a[i-k]+1)
# 없는 경우 10001 (1<=M<=10000)
# 그리디가 아닌 이유 → 큰 단위가 작은 단위의 배수가 아님 

n,m = map(int,input().split())
array = [int(input()) for _ in range(n)]
d = [10001]*(m+1)
d[0] = 0 
 
for idx in array:
  for i in range(idx,len(d)):
    d[i] = min(d[i],d[i-idx]+1) 
 

if d[m] == 10001:
  print(-1)
else:
  print(d[m])
