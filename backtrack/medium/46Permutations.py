# 📖 Problem

# Given an array nums of distinct integers, return all possible permutations.

# 💻 Example
# Input:
# nums = [1,2,3]

# Output:
# [
#  [1,2,3],
#  [1,3,2],
#  [2,1,3],
#  [2,3,1],
#  [3,1,2],
#  [3,2,1]
# ]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutation = []
        used = [False] * len(nums)

        def backtrack():
            if len(permutation) == len(nums):
                result.append(permutation[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                permutation.append(nums[i])

                backtrack()

                permutation.pop()
                used[i] = False

        backtrack()
        return result