class Solution:
    def maxArea(self, height: List[int]) -> int:
        # height=[1,8,6,2,5,4,8,3,7]
        lenh=len(height)
        r=lenh-1
        l=0
        tmparea=0
        while(l<r):
            ans=min(height[l],height[r])
            area=ans*abs(l-r)
            if tmparea<area:
                tmparea=area
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return tmparea
