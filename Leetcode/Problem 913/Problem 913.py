from typing import List
from collections import defaultdict, deque


# cat first and mouse second
# hole stands for node[0]
# 1 for mouse 2 for cat and 0 for none
# mouse starts at 0 and cats start at 1
class Solution:
    Mouse, Cat, Struggle = 1, 2, 0

    def findOpponentParents(self, cur, graph):
        res = []
        mousePov, catPov, turn = cur
        if turn == self.Mouse:
            for catMove in graph[catPov]:
                # cat is not allowed to travel to the hole
                if catMove == 0:
                    continue
                res.append((mousePov, catMove, self.Cat))
        elif turn == self.Cat:
            for mouseMove in graph[mousePov]:
                res.append((mouseMove, catPov, self.Mouse))
        return res

    def findChildern(self, cur, graph, dp):
        mousePov, catPov, turn = cur
        if turn is self.Mouse:
            for nextMouse in graph[mousePov]:
                if dp[nextMouse][catPov][self.Cat] != self.Cat:
                    return False
        elif turn is self.Cat:
            for nextCat in graph[catPov]:
                if nextCat in {0}:
                    continue
                if dp[mousePov][nextCat][self.Mouse] != self.Mouse:
                    return False
        return True

    # we must assign the node both up and down to cover as many points as possible
    def catMouseGame(self, graph: List[List[int]]) -> int:
        # dp [i][j][t] i for cats position and j for mouse position and t for the turn
        # len(graph) stands for the num of the vertices in the graph
        dp = [[[0] * 3 for i in range(len(graph))] for j in range(len(graph))]
        q = deque()

        # initialization
        for i in range(1, len(graph)):
            for t in range(1, 3):
                dp[0][i][t] = self.Mouse
                dp[i][i][t] = self.Cat
                q.append((0, i, t))
                q.append((i, i, t))

        while q:
            front = q.popleft()
            mousePov, catPov, turn = front
            # for all the status that can reach the current state
            for status in self.findOpponentParents(front, graph):
                preMouse, preCat, preTurn = status
                if dp[preMouse][preCat][preTurn] not in {0}:  # already assign
                    continue
                # for cat, once cat can move to a state that the mouse dies, then leading to a mouse's death
                # for mouse, once mouse can move to a state that the cat dies, then leading to a cat's death
                if dp[mousePov][catPov][turn] == preTurn:
                    dp[preMouse][preCat][preTurn] = preTurn
                    q.append((preMouse, preCat, preTurn))
                # the leading result of the node with definite result
                elif self.findChildern(status, graph, dp) is True:
                    dp[preMouse][preCat][preTurn] = 3 - preTurn
                    q.append(status)
            # the remaining unknown state node is for the result
        return dp[1][2][1]


if __name__ == '__main__':
    s = Solution()
    # bug here for dfs :
    graph = [[2, 3], [3, 4], [0, 4], [0, 1], [1, 2]]
    print(s.catMouseGame(graph))
