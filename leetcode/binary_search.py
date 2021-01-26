def binary_search(nums, target):
    lo = 0
    hi = len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo



array = [1,3,5,6,7,7,8]
targets = [0,1,2,3,4,5,6,7,8,9]

for target in targets:
    ans = binary_search(array, target)
    print(f"Searching for {target} in {array} returns {ans}")

