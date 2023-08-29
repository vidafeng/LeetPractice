class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = {}

        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1

        for num in hash:
            if hash[num] == 1:
                return num
