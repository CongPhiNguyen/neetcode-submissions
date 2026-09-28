class Solution:
    def make_key(self, word) -> str:
        counts = {}

        for char in word:
            counts[char] = counts.get(char, 0) + 1

        res = ""
        for key in sorted(counts):
            res += str(counts[key]) + key
        return res

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = {}
        for s in strs:
            key = self.make_key(s)
            if key not in l:
                l[key] = [s]
            else:
                l[key].append(s)

        res = []

        for key in l:
            res.append(l[key])

        return res