class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_s = {}        
        for val in s:
            if val in hash_s: 
                hash_s[val]+=1
            else: hash_s[val] = 1

        for val in t:
            if val in hash_s and hash_s[val] > 0: 
                hash_s[val]-=1
            else: return False;

        return True

