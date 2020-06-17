from typing import *


class Solution:
    def validIPAddress(self, IP: str) -> str:
        import re
        chunk_4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2([0-4][0-9]|5[0-5]))'
        ipv4 = re.compile(
            chunk_4 + '.' + chunk_4 + '.' + chunk_4 + '.' + chunk_4 + '$'
        )
        chunk_6 = r'[0-9a-fA-F]{1,4}'
        ipv6 = re.compile(
            chunk_6 + ':' + chunk_6 + ':' + chunk_6 + ':' +
            chunk_6 + ':' + chunk_6 + ':' + chunk_6 + ':' +
            chunk_6 + ':' + chunk_6 + '$')
        if ipv4.match(IP):
            return "IPv4"
        elif ipv6.match(IP):
            return "IPv6"
        else:
            return "Neither"

sol = Solution()

cases = [
    "172.16.254.1",
    "172.16.254.01",
    "256.256.256.256",
    "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
    "2001:db8:85a3:0:0:8A2E:0370:7334",
    "2001:0db8:85a3::8A2E:0370:7334",
    "02001:0db8:85a3:0000:0000:8a2e:0370:7334"
]

for case in cases:
    print(sol.validIPAddress(case))

