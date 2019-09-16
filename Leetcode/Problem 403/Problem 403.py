from typing import List
from collections import defaultdict

# only one way to reach each state
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dic = defaultdict(set)
        dic[0].add(0)
        for stone in stones:  # for every stone move from start to end
            if stone in dic:  # if current stone is accessible
                for step in dic[stone]:  # for each step accessing stone
                    for diff in [-1, 0, 1]:
                        if step + diff > 0:
                            if stone + step + diff == stones[-1]:
                                return True
                            dic[stone + step + diff].add(step + diff)
        return False


if __name__ == '__main__':
    s = Solution()
    stones = [0, 1, 3, 5, 6, 8, 12, 17]
    print(s.canCross(stones))
