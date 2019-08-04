import sys

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        #  Ensure we are always binary search on the shorter array
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)
        psum = (len1+len2+1)//2
        low = 0
        high = len1
        while low <= high:
            p1 = (low + high)//2
            p2 = psum - p1
            minLeft1 = float('-inf') if (p1 == 0) else nums1[p1-1]
            maxRight1 = float('inf') if (p1 == len1) else nums1[p1]
            minLeft2 = float('-inf') if (p2 == 0) else nums2[p2-1]
            maxRight2 = float('inf') if (p2 == len2) else nums2[p2]
            #  We found the correct partition
            if minLeft1 <= maxRight2 and minLeft2 <= maxRight1:
                #  if combined is odd array, middle element
                if (len1 + len2) % 2 == 1:
                    return max(minLeft1, minLeft2)
                #  combined is even array, average of middle two elements
                else:
                    return (max(minLeft1, minLeft2) + min(maxRight1, maxRight2))/2
            elif minLeft1 > maxRight2:
                # move p1 to the left
                high = p1 - 1
            else:
                # move p1 to the right
                low = p1 + 1
    
def main():
    print("hello world")
    s = Solution()    # a = s.findMedianSortedArramax(minLeft1, minLeft2)ys([1], [2])
    # print("expecting 1.5, getting", a)

    a = s.findMedianSortedArrays([1, 3], [2])
    print("expecting 2, getting", a)

    a = s.findMedianSortedArrays([1, 3], [2, 4])
    print("expecting 2.5, getting", a)

if __name__ == "__main__":
    main()
        
