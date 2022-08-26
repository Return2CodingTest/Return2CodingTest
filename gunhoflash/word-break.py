from typing import List

class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    length = len(s)

    # isbreakable[i] represents that s[0:i] can be segmented into
    # a space-separated sequence of one or more dictionary words.
    isbreakable = [False] * (length + 1)
    isbreakable[0] = True

    for i in range(1, length + 1):
      # for each word,
      for word in wordDict:
        wordLength = len(word)
        # if s[0:i] was ended with the word, sync breakability
        if i - wordLength >= 0:
          if isbreakable[i - wordLength] and s[i - wordLength : i] == word:
            isbreakable[i] = True
            break

    return isbreakable[length]
