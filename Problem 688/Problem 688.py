# possibility of still remaining on the board
# N: size of the board
# K: the possible moving steps
# r: the initial row
# c: the initial col
import functools

class Solution:
    movement = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, -1), (-2, 1), (-1, 2), (-1, -2)]
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        @functools.lru_cache(None)
        def dp(row, col, step):
            if row < 0 or row >= N or col < 0 or col >= N:
                return 0
            elif step == 0:
                return 1
            else:
                res = sum([dp(row + r, col + c, step - 1) for r, c in self.movement]) / 8.0
                return res
        return dp(r, c, K)


if __name__ == '__main__':
    s = Solution()
    N = 3
    k = 2
    r = 0
    c = 0
    print(s.knightProbability(N, k, r, c))
