class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l=[]
        for i in tokens:
            if i.lstrip('-').isdigit():
                l.append(int(i))
            else:
                b=l.pop()
                a=l.pop()
                if i=='+' :
                    l.append(a+b)
                elif i=='-' :
                    l.append(a-b)
                elif i=='*' :
                    l.append(a*b)
                elif i=='/' :
                    l.append(int(a/b))
        return int(l[0])