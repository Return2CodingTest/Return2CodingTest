class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        anagrams = []
        for word1 in strs:
            isAppended = False
            for i in range(len(anagrams)):
                 if anagrams[i] == Counter(word1):
                        ans[i].append(word1)
                        isAppended = True
                        break
            if not isAppended:
                ans.append([word1])
                anagrams.append(Counter(word1))
        return ans