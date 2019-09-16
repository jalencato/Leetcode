from typing import List
from collections import defaultdict


# words contain the first letter of the puzzles
# all the letters in the words are in the puzzles
class Solution:
    def getMask(self, word: str) -> int:
        mask = 0
        for c in word:
            i = ord(c) - ord('a')
            mask |= 1 << i
        return mask

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        letterCount = defaultdict(lambda: int(0))
        for word in words:
            mask = self.getMask(word)
            letterCount[mask] = letterCount[mask] + 1

        solution = [0] * len(puzzles)
        count = 0

        for puzzle in puzzles:
            mask = self.getMask(puzzle)
            subMask = mask
            total = 0

            firstBitIndex = ord(puzzle[0]) - ord('a')

            # making use of the hashing table
            while True:
                if subMask >> firstBitIndex & 1:
                    total += letterCount.get(subMask, 0)
                if subMask == 0:
                    break
                subMask = (subMask - 1) & mask
            solution[count] = total
            count += 1
        return solution


if __name__ == '__main__':
    s = Solution()
    words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access", "access"]
    puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
    print(s.findNumOfValidWords(words, puzzles))
