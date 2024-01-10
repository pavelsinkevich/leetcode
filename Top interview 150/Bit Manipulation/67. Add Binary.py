'''Given two binary strings a and b, return their sum as a binary string.'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l = max(len(a), len(b)) + 1
        a = a.zfill(l)
        b = b.zfill(l)
        res = [0]*l
        prev = 0
        for i in reversed(range(l)):
            res[i] = (int(a[i]) + int(b[i]) + prev) % 2
            prev = (int(a[i]) + int(b[i]) + prev) // 2
        if l > 1:
            if res[0] == 0:
                del res[0]
        return ''.join(str(item) for item in res)
    
obj = Solution()
a = "11"
b = "1"
print(obj.addBinary(a, b))