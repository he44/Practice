from typing import *

"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        read_num = 0
        buf4 = ['' for _ in range(4)]
        actual_read = 4
        while read_num < n and actual_read == 4:
            actual_read = read4(buf4)
            for k in range(actual_read):
                if read_num == n:
                    return read_num
                buf[read_num] = buf4[k]
                read_num += 1
        return read_num