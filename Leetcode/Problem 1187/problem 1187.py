from collections import defaultdict
import bisect

# Actually it is a kind of simulate it is not a divide programming
class Solution:
    def makeArrayIncreasing(self, arr1, arr2) -> int:
        state = {-1: 0} #position: number of methods
        arr2.sort()
        for val in arr1:
            tmp = defaultdict(lambda: float('inf'))
            for key in state:
                if val > key:
                    tmp[val] = min(tmp[val], state[key])
                loc = bisect.bisect_right(arr2, key)
                if loc < len(arr2):
                    tmp[arr2[loc]] = min(tmp[arr2[loc]], state[key] + 1)
            state = tmp
        if state:
            return min(state.values())
        return -1


if __name__ == '__main__':
    s = Solution()
    arr1 = [1, 5, 3, 6, 7]
    arr2 = [1, 3, 2, 4]
    print(s.makeArrayIncreasing(arr1, arr2))
