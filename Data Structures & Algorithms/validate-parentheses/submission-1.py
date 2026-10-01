class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in '[{(':
                st.append(c)
            else:
                if len(st) == 0:
                    return False
                l = st.pop()
                if (
                    c == ']' and l != '['
                    or c == '{' and l != '}'
                    or c == ')' and l != '('
                ):
                    return False
        return len(st) == 0
                    