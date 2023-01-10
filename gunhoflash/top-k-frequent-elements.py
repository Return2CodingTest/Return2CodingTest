from collections import Counter
from typing import List

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    return list(
      map(
        lambda v : v[0],
        Counter(nums).most_common(k)
      )
    )
