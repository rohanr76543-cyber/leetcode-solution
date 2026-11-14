class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        sumNumsl=sum(nums)
        leftSum=[]
        rightSum=[]
        n=len(nums)
        for i in range(n-1,-1,-1):
            sumNumsl=sumNumsl-nums[i]
            leftSum.insert(0,sumNumsl)
        sumNumsr=sum(nums)
        for num in nums:
            sumNumsr=sumNumsr-num
            rightSum.append(sumNumsr)
        res=[]
        for i in range(n):
            res.append(abs(rightSum[i]-leftSum[i]))
        return res    