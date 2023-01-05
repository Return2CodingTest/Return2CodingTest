import re

# Time Limit Exceeded

class WordDictionary:
    words = set()

    def __init__(self):
        self.words = set()

    def addWord(self, word: str) -> None:
        self.words.add(word)

    def search(self, word: str) -> bool:
        if word in self.words:
            return True
        regex = re.compile(word)
        for el in self.words:
            res = regex.fullmatch(el)
            if res:
                return True
        return False