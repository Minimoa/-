n,m = map(int,input().split(" "))
x,y,direction =  map(int,input().split(" "))

location = [list(map(int,input().split(" "))) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
visited[x][y] = True
 

#북 , 동, 남, 서
dx = [-1,0,1,0]
dy = [-0,1,0,-1]

#왼쪽으로 회전
def turn_left():
  global direction 
  direction -= 1
  if direction == -1:
    direction = 3

move = 1
turn_time = 0

while 1:
  turn_left()
  nx = x+dx[direction]
  ny = y+dy[direction]

  if not visited[nx][ny] and location[nx][ny] == 0:
    visited[nx][ny] = True
    x = nx
    y = ny
    move += 1
    turn_time = 0 
    continue

  else:
    turn_time += 1
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    if location[nx][ny] == 0:
      x = nx
      y = ny
    else:
      break
    turn_time = 0
 
print(move)
