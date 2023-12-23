def func(son):
    raqam=son
    res1=son%10
    res2=res1
    son=son//10
    
    while son>0:
        res1=son%10
        son=son//10
        res2=res2*10
        res2=res2+res1
        
    if raqam==res2:
        return "True"
    else:
        return "False"

print(func(123))