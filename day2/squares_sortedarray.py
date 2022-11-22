def sortedArraysquares(nums: list[int]) -> list:
    positive_array=list(map(lambda x : -(x) if x<0 else x,nums))
    

print(sortedArraysquares([-7,-3,2,3,11]))