class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet_count = Counter(s)
        for alp in t:
            if alp in alphabet_count:
                alphabet_count[alp]-=1
            else:
                return False
        for alp in alphabet_count:
            if alphabet_count[alp]:
                return False
        return True