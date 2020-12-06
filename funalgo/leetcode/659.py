
# 122234567 123 245 267
class Solution:
    def isPossible(self, nums: list) -> bool:
        max_num = max(nums)
        counter = [0] * max_num
        for n in nums:
            counter[n] += 1
        temp = []
        i = 0
        while i < max_num:
            if counter[i] == 2:
