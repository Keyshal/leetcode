class Solution:
    def part2(self, nums, left, right, target, reslist):

        if left >= right:
            if left == right and nums[left] == target:
                reslist.append(left)
            return
        if target == nums[left]:
            reslist.append(left)
        if target == nums[right]:
            reslist.append(right)
        mid = left + (right - left) // 2
        if target == nums[mid]:
            reslist.append(mid)
        if target <= nums[mid]:
            self.part2(nums, left, mid - 1, target, reslist)
        if target >= nums[mid]:
            self.part2(nums, mid + 1, right, target, reslist)

    def search(self, nums: List[int], target: int) -> List[int]:
        # target = 6
        left = 0
        right = len(nums) - 1
        reslist = []
        # res = []
        res=0
        lid = nums.index(min(nums))
        left = 0
        right = len(nums) - 1
        if target>=nums[lid] and target<=nums[right]:
            self.part2(nums, lid, right, target,reslist)
        if target<=nums[lid-1] and target>=nums[left]:
            self.part2(nums, 0, lid, target, reslist)
        if reslist == []:
            res=-1
            # res.append(-1)
            # res.append(-1)
        else:
            res=min(reslist)
            # res.append(min(reslist))
            # res.append(max(reslist))
        return res
