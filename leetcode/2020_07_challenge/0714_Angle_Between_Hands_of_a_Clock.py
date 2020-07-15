from typing import *


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_hour = (hour * 360 / 12.0 + 30.0 * minutes / 60) % 360
        angle_minute = minutes * 360 / 60.0
        angle = max(angle_hour, angle_minute) - min(angle_hour, angle_minute)
        return min(angle, 360-angle)

cases = [
    (12, 30),
    (3, 30),
    (3, 15),
    (4, 50),
    (12, 0)
]

sol = Solution()

for case in cases:
    print(sol.angleClock(case[0], case[1]))