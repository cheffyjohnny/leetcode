import time

def print_board(board, path):
    print()

    for r in range(len(board)):
        row = ""

        for c in range(len(board[0])):
            if (r, c) in path:
                row += f"[{board[r][c]}]"
            else:
                row += f" {board[r][c]} "

        print(row)

    print()

class Solution:
    def exist(self, board, word):

        ROWS = len(board)
        COLS = len(board[0])

        visited = set()
        path = []

        def dfs(row, col, index):

            # Show current state
            print("Searching:")
            print(" -> ".join(board[r][c] for r, c in path))
            print_board(board, path)

            time.sleep(1)


            # Success
            if index == len(word):
                print("FOUND! 🎉")
                return True


            # Invalid
            if (
                row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                board[row][col] != word[index] or
                (row, col) in visited
            ):
                print("FAILED ❌")
                return False


            # Choose
            visited.add((row, col))
            path.append((row, col))


            # Explore
            found = (
                dfs(row - 1, col, index + 1) or
                dfs(row + 1, col, index + 1) or
                dfs(row, col - 1, index + 1) or
                dfs(row, col + 1, index + 1)
            )


            # Backtrack
            visited.remove((row, col))
            path.pop()

            print("BACKTRACK ↩️")
            print_board(board, path)

            time.sleep(1)


            return found


        for row in range(ROWS):
            for col in range(COLS):

                if dfs(row, col, 0):
                    return True

        return False

board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]

word = "ABCCED"

solution = Solution()

result = solution.exist(board, word)

print("Result:", result)