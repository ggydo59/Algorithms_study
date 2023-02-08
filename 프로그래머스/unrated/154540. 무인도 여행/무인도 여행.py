import sys
sys.setrecursionlimit(10**5)
def solution(maps):
    answer = []
    maps = [list(map(int, i.replace("X", "0"))) for i in maps ]
    w, h = len(maps[0]), len(maps)
    area = 0
    def dfs(r,c):
        if r < 0 or c < 0 or r >= w or c >= h:
            return 0
    
        if maps[c][r] == 0:
            return 0
    
        temp, maps[c][r] = maps[c][r], 0
        return temp + dfs(r, c+1) + dfs(r, c-1) + dfs(r+1, c) + dfs(r-1, c)

    for i in range(w):
          for j in range(h):
            area = dfs(i,j)    
            if area > 0:
                answer.append(area)
    
    return sorted(answer) if answer else [-1]
