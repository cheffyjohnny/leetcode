# 📖 Problem

# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets.

# 💻 Example
# Input:
# nums = [1,2,3]

# Output:
# [
#  [],
#  [1],
#  [2],
#  [3],
#  [1,2],
#  [1,3],
#  [2,3],
#  [1,2,3]
# ]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(start):
            result.append(subset[:])

            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()

        backtrack(0)
        return result