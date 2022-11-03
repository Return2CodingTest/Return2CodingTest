class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    for char in s:
      match char:
        case '(' | '{' | '[':
          stack.append(char)
        case ')':
          if len(stack) == 0 or stack.pop() != '(':
            return False
        case '}':
          if len(stack) == 0 or stack.pop() != '{':
            return False
        case ']':
          if len(stack) == 0 or stack.pop() != '[':
            return False
    return len(stack) == 0
