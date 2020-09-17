from typing import *

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = (0,0)
        dirc = 0
        move = {
            0: (0,1),
            1: (1,0),
            2: (0, -1),
            3: (-1, 0)
        }
        for instruction in instructions:
            if instruction == "G":
                pos = (pos[0] + move[dirc][0], pos[1]  + move[dirc][1])
            elif instruction == "L":
                dirc -= 1
                if dirc < 0:
                    dirc += 4
            elif instruction == "R":
                dirc += 1
                if dirc > 3:
                    dirc -= 4
        return(pos == (0,0) or dirc != 0)


        
