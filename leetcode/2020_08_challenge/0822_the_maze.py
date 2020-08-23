from typing import *

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        def all_the_way(maze, cur, direction):
            r = len(maze)
            c = len(maze[0])
            # the current one must be empty
            nx, ny = cur[0], cur[1]
            while 0 <= nx < r and 0 <= ny < c and maze[nx][ny] == 0:
                nx += direction[0]
                ny += direction[1]
            return [nx - direction[0], ny - direction[1]]

        # the issue is once you move you cannot stop
        def dfs(cur, visited):
            if cur == destination:
                return True
            cx, cy = cur
            # try different directions
            visited[cx][cy] = True
            # up, right, down, left
            for direc in [[-1,0], [0,1], [1, 0], [0,-1]]:
                new_point = all_the_way(maze, cur, direc)
                if not visited[new_point[0]][new_point[1]] and dfs(new_point, visited):
                    return True


        r = len(maze)
        c = len(maze[0])
        visited = [[False for x in range(c)] for y in range(r)]
        return dfs(start, visited)



            

