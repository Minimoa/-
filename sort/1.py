n = int(input())
array = [input() for _ in range(n)]
array.sort(reverse=True)
print(list(map(int,array)))
