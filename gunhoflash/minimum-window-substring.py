class CharCount:
  def __init__(self):
    self.now = 0
    self.need = 0

class Solution:
  def minWindow(self, s: str, t: str) -> str:
    charCountMap = {}

    # init CharCount from A to Z and a to z
    for i in range(26):
      charCountMap.setdefault(chr(65 + i), CharCount())
      charCountMap.setdefault(chr(97 + i), CharCount())

    # init need count
    for char in t:
      charCountMap.get(char).need += 1

    # count the number of unsatisfied char
    nUnsatisfiedChar = len(list(filter(lambda v: v.need > 0, charCountMap.values())))

    answer = ''
    left = 0
    for right, rightChar in enumerate(s):
      rightCharCount = charCountMap.get(rightChar)

      rightCharCount.now += 1
      if rightCharCount.now == rightCharCount.need:
        nUnsatisfiedChar -= 1

      if nUnsatisfiedChar != 0: continue

      # ready to shirink
      while True:
        leftCharCount = charCountMap.get(s[left])

        # delete unnecessary char from left
        if leftCharCount.now > leftCharCount.need:
          leftCharCount.now -= 1
          left += 1
        else:
          # update answer
          if len(answer) == 0 or len(answer) > right - left + 1:
            answer = s[left : right + 1]
          break

    return answer
