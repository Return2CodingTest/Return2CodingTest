class Trie:
  def __init__(self):
    self.hasValue = False
    self.subTrie = {}

  def insert(self, word: str) -> None:
    if len(word):
      firstLetter = word[0]
      subTrie = self.subTrie.setdefault(firstLetter, Trie())
      subTrie.insert(word[1:])
    else:
      self.hasValue = True

  def search(self, word: str) -> bool:
    if len(word):
      firstLetter = word[0]
      subTrie = self.subTrie.get(firstLetter)
      return subTrie is not None and subTrie.search(word[1:])
    else:
      return self.hasValue

  def startsWith(self, prefix: str) -> bool:
    if len(prefix):
      firstLetter = prefix[0]
      subTrie = self.subTrie.get(firstLetter)
      return subTrie is not None and subTrie.startsWith(prefix[1:])
    else:
      return self.hasValue or len(self.subTrie) > 0
