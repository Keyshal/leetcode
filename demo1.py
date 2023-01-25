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

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # target = 6
        res = True
        # matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        reslist = []
        for i in matrix:
            nums = i
            left = 0
            right = len(nums) - 1
            self.part2(nums, left, right, target, reslist)
        if reslist == []:
            res=False
            # res.append(-1)
            # res.append(-1)
        else:
            res=True
        return res
