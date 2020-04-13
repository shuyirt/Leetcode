class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find pivot point
        if not nums:
            return -1
        
        left = 0
        right = len(nums)-1
        
        if right == 0:
            return 0 if nums[0] == target else -1
        if nums[left] < nums[right]:
            pivot = 0
        else:
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    break
                elif nums[pivot] < nums[left]:
                    right = pivot - 1
                else:
                    left = pivot + 1
        
        pivot = pivot + 1  
        
        if target >= nums[pivot] and target <= nums[-1]:
            right = len(nums)-1
            left = pivot
        else:
            right = pivot
            left = 0
        
        while left <= right: 
            pivot = (left+right)//2
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] >= target:
                right = pivot-1
            else:
                left = pivot+1
            # print(left, right, pivot)
        return -1

# Runtime: 32 ms, faster than 95.21% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 13.3 MB, less than 40.34% of Python3 online submissions for Search in Rotated Sorted Array.