from typing import *

class Solution:
    def validIPAddress(self, IP: str) -> str:
        hexdecimal = ['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']
        if IP.find('.') != -1:
            tip = "IPv4"
            numbers = IP.split('.')
            if len(numbers) != 4:
                return "Neither"
            for number in numbers:
                if len(number) == 0:
                    return "Neither"
                if len(number) >=2 and number[0] == '0':
                    return "Neither"
                if not number.isdigit() or int(number) > 255 or int(number) < 0:
                    return "Neither"
            return tip
        elif IP.find(':') != -1:
            tip = "IPv6"
            numbers = IP.split(':')
            if len(numbers) != 8:
                return "Neither"
            for number in numbers:
                if len(number) > 4 or len(number) == 0:
                    return "Neither"
                for char in number:
                    if (not char.isdigit()) and (char not in hexdecimal):
                        return "Neither"
            return tip
        else:
            tip = "Neither"
            return tip

            
sol = Solution()

cases = [
    "172.16.254.1",
    "2001:0db8:85a3:0:0:8A2E:0370:7334",
    "256.256.256.256"
]

for case in cases:
    print(sol.validIPAddress(case))

        
