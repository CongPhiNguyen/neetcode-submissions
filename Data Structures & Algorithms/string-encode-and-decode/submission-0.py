class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0
        j = 1

        res = []

        while j < len(s):
            while s[j] != '#':
                j+=1
            print(s[i:j])
            count = int(s[i:j])
            res.append(s[j+1:j+count+1])
            i = j+count+1
            j = i + 1

        return res




        