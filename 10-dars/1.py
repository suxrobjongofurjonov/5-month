
def number(nums):
           nums.sort()

           if nums[0]!= 0:
            return 0

           for i in range(len(nums)-1):
                if nums[i] + 1 == nums[i+1]:
                    continue
                else:
                    return nums[i] + 1
                
print(number([3,0,1]))