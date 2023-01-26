class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        nums=[-999999999999999999999999]+nums
        nums=nums+[-999999999999999999999999]
        lenn = len(nums)
        res = []
        for i in range(0, lenn - 2):
            tmp = nums[i:i + 3]
            z = nums[i + 1]
            h = nums[i + 2]
            if nums[i + 1] > nums[i] and nums[i + 1] > nums[i + 2]:
                res.append(i)
        if len(res)>0:
            return min(res)
        else:
            if lenn==1:
                return 0
            else:
                return max(nums)
