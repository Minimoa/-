 

n,m = map(int,input().split(" "))
graph = [list(map(int,input())) for _ in range(n)] 

dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 0

def dfs(x,y):
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return False
  
  if graph[x][y] == 0:
    graph[x][y] = 1
    for i in range(4):
      dfs(x+dx[i],y+dy[i])
    return True
  return False

for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      if dfs(i,j):
        cnt += 1




print(cnt)
