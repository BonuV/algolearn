#simple solution


#solution 1 ---
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            out = nums.index(target)
        except:
            out=-1
        return out

#solution 2 ---
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        out=-1
        
        while low<=high:
            mid=low+high
            if nums[mid]==target:
                out= mid
                break;
            elif nums[mid]< target:
                low=mid+1
            elif nums[mid]> target:
                high=mid-1
        return out