# each word is 6 letters long
# one word as secret
# expectation and filter thoughts are essential
class Solution(object):
    def findSecretWord(self, wordlist, master):
        wordSet = set(wordlist)
        for _ in range(10):
            if not wordSet:
                return
            word = wordSet.pop()
            cnt = master.guess(word)
            def check(other):
                return sum(1 if other[i] == word[i] else 0 for i in range(6)) == cnt
            wordSet = set(filter(check, wordSet))


if __name__ == '__main__':
    s = Solution()
    print(s.findSecretWord())