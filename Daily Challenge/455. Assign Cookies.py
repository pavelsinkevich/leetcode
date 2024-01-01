'''Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. 
If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. 
Your goal is to maximize the number of your content children and output the maximum number.'''
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        current_child = 0
        for i in range(len(s)):
            if s[i] >= g[current_child]:
                current_child += 1
                if current_child >= len(g):
                    return current_child
        return current_child
        
g = [1,2,3]
s = [1,1]
obj = Solution()
print(obj.findContentChildren(g, s))