def searchInsert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
        
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid -1
    
    return left


pos_val = searchInsert([1,3,5,7],0)
print(pos_val)