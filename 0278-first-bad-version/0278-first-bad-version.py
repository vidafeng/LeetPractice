# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # two pointers left and right
        # left = 1, right = n
        # at each iteration, we compute the midpoint mid of the range
            # left + right / 2 
        # check API to check version
        # if API returns true (version is bad)
        # first bad version must be in left range [left, mid]
            # update right = mid
        # else bad version must be in right range
            # update left = mid+1
        # continue until left and right converge

        left = 1
        right = n

        while left < right: 
            mid = left + (right-left) // 2

            if isBadVersion(mid):
                right = mid
            else: 
                left = mid+1
        return left

