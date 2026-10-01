class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for val in tokens:
            if val not in "+-*/":
                s.append(int(val))
            else:
                a = s.pop()
                b = s.pop()
                match val:
                    case "+": s.append(a+b)
                    case "-": s.append(b-a)
                    case "/": s.append(int(b/a))
                    case "*": s.append(a*b)
        return s[0]