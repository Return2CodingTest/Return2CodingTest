from typing import List

def charToInt(c):
  return ard[c] - 97

def getFirstDiffLetters(a, b):
  index = next((i for i in range(min(len(a), len(b))) if a[i] != b[i]), None)
  if index is not None:
    return [a[index], b[index]]
  return None

class Letter:
  def __init__(self, value):
    self.value = value
    self.isUsed = False
    self.before = set()
    self.after = set()

class Solution:
  def alien_order(self, words: List[str]) -> str:

    letters = dict()

    for i in range(26):
      letters[chr(i + 97)] = Letter(chr(i + 97))

    prevWord = ''
    for word in words:
      for c in word:
        letters.get(c).isUsed = True

      diffLetters = getFirstDiffLetters(prevWord, word)
      if diffLetters:
        [ahead, behind] = diffLetters
        aheadLetter = letters.get(ahead)
        behindLetter = letters.get(behind)
        aheadLetter.after.add(behindLetter)
        behindLetter.before.add(aheadLetter)

      prevWord = word

    # delete not used letters
    letters = dict(filter(lambda pair: pair[1].isUsed, letters.items()))

    answer = ''
    while len(letters):
      lettersWithoutBefore = list(filter(lambda letter: len(letter.before) == 0, letters.values()))
      if len(lettersWithoutBefore) == 0: break
      lettersWithoutBefore = sorted(lettersWithoutBefore, key=lambda letter: letter.value)
      for letter in lettersWithoutBefore:
        letters.pop(letter.value)
        answer += letter.value
        for l in letter.after:
          l.before.remove(letter)

    return '' if len(letters) > 0 else answer
