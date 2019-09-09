import copy
from typing import Dict, Any


class Solution(object):
    def findSubstring(self, s, words):
        if len(words) == 0:
            return []
        single = len(words[0])
        lengthTotal = len(words)*len(words[0])
        result = []

        wordState: Dict[Any, bool] = {}
        for c in words:
            wordState[c] = False

        iter = 0
        while iter <= len(s) - lengthTotal:
            tmp = copy.deepcopy(s[iter:iter + lengthTotal])
            for c in words:
                wordState[c] = False
            inter = 0
            while True:
                if wordState.get(tmp[inter: inter + single]) is not None and wordState[tmp[inter: inter + single]] in {False}:
                    wordState[tmp[inter:inter+single]] = True
                    inter += single
                else:
                    break

            res = True
            if any(v == False for v in wordState.values()):
                res = False
                iter += 1
            if res is True:
                result.append(iter)
                iter += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.findSubstring("wordgoodgoodgoodbest", ['bar', 'foo']))
