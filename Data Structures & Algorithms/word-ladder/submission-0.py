from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)

        pattern_to_words = collections.defaultdict(list)

        for word in wordList:
            for char in range(0, len(word)):
                pattern = word[:char] + "*" + word[char+1:]
                pattern_to_words[pattern].append(word)
        
        visited = set([beginWord]) #track visisted nodes
        q = deque()
        q.append(beginWord)
        result = 1

        while q:
            for i in range(0, len(q)):
                curr_word = q.popleft() #for BFS -- layer by layer
                if curr_word == endWord:
                    return result
                for char in range(0, len(curr_word)):
                    pattern = curr_word[:char] + "*" + curr_word[char+1:]
                    for neigh in pattern_to_words[pattern]:
                        if neigh not in visited:
                            q.append(neigh)
                            visited.add(neigh)
            result += 1 
        return 0


        