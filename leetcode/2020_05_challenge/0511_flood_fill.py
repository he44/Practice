from typing import *


class Solution:
	def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
		def fill(image, sr, sc, oc, nc):
			print(sr, sc)
			ci = [-1, 1, 0, 0]
			ri = [0, 0, -1, 1]
			if image[sr][sc] != oc or oc == nc:
				return
			image[sr][sc] = nc
			for n in range(4):
				r = sr + ri[n]
				c = sc + ci[n]
				if r < len(image) and c < len(image[0]) and r >= 0 and c >= 0 and image[r][c] == oc:
					fill(image, r, c, oc, nc)
			return
		fill(image, sr, sc, image[sr][sc], newColor)
		return image

def main():
	s = Solution()
	image = [[1,1,1],[1,1,0],[1,0,1]]
	#image =[[0,0,0],[0,1,1]]
	output = s.floodFill(image, 1, 1, 2)
	print(output)

if __name__ == "__main__":
	main()
        
