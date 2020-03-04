class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights=[0]+heights+[0]
        a=[]
        m=0
        for i in range(len(heights)):
            while a and heights[a[-1]]>heights[i]:
                k=a.pop()
                m=max(m,(i-a[-1]-1)*heights[k])
            a.append(i)
        return m
