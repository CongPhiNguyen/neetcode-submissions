class Solution:
    def make_key(self, word: str) -> tuple[int, ...]:
        counts = [0] * 26
        for char in word:
            counts[ord(char) - ord("a")] += 1
        return tuple(counts)

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