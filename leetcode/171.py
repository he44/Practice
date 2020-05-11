from typing import *

class Solution:
	def titleToNumber(self, s: str) -> int:
		count = 0
		for i in range(len(s)):
			idx = ord(s[i]) - ord('A') + 1
			count += idx * (26 ** (len(s) - i - 1))
		return count

def main():
	s = Solution()
	tests = ['A', 'C', 'Z', 'AA', 'AB', 'AZ']
	for test in tests:
		print("%s-->%d"%(test, s.titleToNumber(test)))

if __name__ == "__main__":
	main()
