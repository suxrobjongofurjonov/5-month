def func(nums, target):
        a=0
        b=len(nums)-1
        while a<=b:
            res=(a+b)//2
            if nums[res]<target:
                a=res+1
            elif nums[res]>target:
                b=res-1
            else:
                return res
        return a
    
print(func(nums=[1,2,3,4], target=6))