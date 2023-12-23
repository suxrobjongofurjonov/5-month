def add_func(a,b):
    res=a[0]+b[0]
    res2=a[1]+b[1]
    res3=a[2]+b[2]
    natija= str(res) + str(res2) + str(res3)
    return int(natija)

print(add_func([1,1,1],[2,2,2]))
        