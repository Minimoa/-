#1
n = int(input())
array = [input() for _ in range(n)]
array.sort(reverse=True)
print(list(map(int,array)))

#2
n = int(input())
array = [input().split() for _ in range(n)]
print(" ".join([data[0] for data in sorted(array,key=lambda x: x[1])]))


#3
n,k = map(int,input().split())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())),reverse=True)

for i in range(k):
  if a[i]<b[i]:
    a[i],b[i] = b[i],a[i]
  else:
    break
print(sum(a))
