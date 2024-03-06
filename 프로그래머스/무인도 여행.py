from collections import deque
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def solution(maps):
    answer = []
    arrs = []
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    print(visited)
    def bfs(x,y):
        now = []
        q = deque()
        q.append(x,y)
        visited[i][j] = 1
        maxnum = maps[x][y]
        while q :
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 and nx>=len(maps) and ny<0 and ny<=len(maps[0]):
                    continue
                if maps[nx][ny] == "X" :
                    continue
                if visited[nx][ny] == 1:
                    continue
                maps[nx][ny] += maps[x][y]
                maxnum = max(maxnum,maps[nx][ny])
        return maxnum
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X":
                arrs.append(bfs(i,j))
                        
    return sorted(arrs)