class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordDict = set(wordList)
        if endWord not in wordDict: return 0

        s1, s2 = {beginWord}, {endWord}
        step = 1
        wordDict.remove(endWord)
        if beginWord in wordDict: wordDict.remove(beginWord)

        while len(s1) > 0 and len(s2) > 0:
            if len(s1) > len(s2): s1, s2 = s2, s1
            step += 1
            next_s1 = set()

            for w in s1:
                # generate each possible transform for w.
                for i in range(len(w)):
                    # trasformation in Locationi for w
                    new_words = [w[:i] + t + w[i + 1:] for t in string.ascii_lowercase]
                    for new_word in new_words:
                        if new_word in s2:
                            return step
                        elif new_word in wordDict:
                            next_s1.add(new_word)
                            wordDict.remove(new_word)
            s1 = next_s1

        return 0