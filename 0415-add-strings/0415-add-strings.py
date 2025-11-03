class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        max_len = max(len(num1), len(num2))
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)

        carry = 0
        res = []

        for i in range(max_len - 1, -1, -1):
            total = int(num1[i]) + int(num2[i]) + carry
            res.append(str(total % 10))
            carry = total // 10

        if carry:
            res.append(str(carry))
        return ''.join(res[::-1])
