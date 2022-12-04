from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myD = defaultdict(list)
        for str in strs :
            myD["".join(sorted(str))].append(str)
            
        return list(myD.values())
