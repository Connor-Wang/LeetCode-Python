class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            j = dic.get(target - num)
            if j is not None and j != i:
                return [j, i]
            dic[num] = i

s = Solution()
nums = [3, 3]
target = 6
print(s.twoSum(nums, target))
