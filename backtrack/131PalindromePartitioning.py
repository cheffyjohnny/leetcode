# 📖 Problem

# Given a string s, partition it so that every substring is a palindrome.

# Return all possible palindrome partitions.

# 💻 Example
# Input:
# s = "aab"

# Output:
# [
#  ["a","a","b"],
#  ["aa","b"]
# ]

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        partition = []

        def isPalindrome(string):
            return string == string[::-1]

        def backtrack(start):
            if start == len(s):
                result.append(partition[:])
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                if not isPalindrome(substring):
                    continue

                partition.append(substring)
                backtrack(end)
                partition.pop()

        backtrack(0)
        return result


# []
# ├── take "a"
# │   │
# │   ├── take "a"
# │   │   │
# │   │   └── take "b"
# │   │
# │   └── done
# │
# ├── take "aa"
# │   │
# │   └── take "b"
# │
# └── ignore "aab"