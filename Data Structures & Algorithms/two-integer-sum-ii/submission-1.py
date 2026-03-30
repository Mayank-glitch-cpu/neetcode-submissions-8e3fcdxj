class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n= len(numbers)
        head=0
        tail= n-1
        while head<tail:
            if numbers[head]+numbers[tail]<target:
                head+=1
            elif numbers[head] + numbers[tail] > target:
                tail-=1
            else:
                return [head+1,tail+1]

