from collections import defaultdict
class WordDictionary:

    def __init__(self):
        
        self.wordDict = defaultdict(list)
        

    def addWord(self, word: str) -> None:
        
        if len(word) in self.wordDict:
            self.wordDict[len(word)].append(word)
        else:
            self.wordDict[len(word)] = [word]
        

    def search(self, word: str) -> bool:
        
        if word == None:
            return False
        if '.' not in word:
            return word in self.wordDict[len(word)]
        for v in self.wordDict[len(word)]:
            for i, ch in enumerate(word):
                if v[i] != ch and ch != '.':
                    break
            else:
                return True
        return False
        
