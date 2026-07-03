from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """回溯 + 列/对角线冲突检测：O(n!) 时间，O(n^2) 空间"""
        res, board = [], ["." * n for _ in range(n)]
        cols, diag1, diag2 = set(), set(), set()

        def backtrack(row: int) -> None:
            if row == n:
                res.append(board[:])
                return
            for col in range(n):
                d1, d2 = row - col, row + col
                if col in cols or d1 in diag1 or d2 in diag2:
                    continue
                cols.add(col)
                diag1.add(d1)
                diag2.add(d2)
                board[row] = "." * col + "Q" + "." * (n - col - 1)
                backtrack(row + 1)
                cols.remove(col)
                diag1.remove(d1)
                diag2.remove(d2)

        backtrack(0)
        return res


class Solution2:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        col = [0] * n

        def valid(r, c):
            # 枚举0-r-1的行
            for R in range(r):
                C = col[R]
                if r + c == R + C or r - c == R - C:
                    return False
            return True

        def dfs(r, s):
            if r == n:
                ans.append(["." * c + "Q" + "." * (n - 1 - c) for c in col])
                return
            for c in s:
                if valid(r, c):
                    col[r] = c
                    dfs(r + 1, s - {c})

        dfs(0, set(range(n)))
        return ans


# --- 本地测试 ---
if __name__ == "__main__":
    print(Solution().solveNQueens(4))
