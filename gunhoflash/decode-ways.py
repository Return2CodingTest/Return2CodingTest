class Solution:
  def isDecodable(self, s: str) -> bool:
    if s[0] == '0':
      return False
    num = int(s)
    return 0 < num and num < 27

  def numDecodings(self, s: str) -> int:
    # there is one way to decode empty string
    answerPrev = 1

    # there is one(or zero) way to decode last character only
    answerNow = 1 if self.isDecodable(s[-1]) else 0

    i = len(s) - 1
    while i:
      i -= 1
      answerPrevPrev = answerPrev
      answerPrev = answerNow
      answerNow = (
        # decode 1 character
        answerPrev if self.isDecodable(s[i: i + 1]) else 0
      ) + (
        # decode 2 characters
        answerPrevPrev if self.isDecodable(s[i: i + 2]) else 0
      )

    return answerNow
