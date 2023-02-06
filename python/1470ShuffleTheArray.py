class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [0] * len(nums)
        for i in range(n):
            res[2 * i] = nums[i]
            res[2 * i + 1] = nums[n + i]
        return res
