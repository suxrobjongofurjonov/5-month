import random
def func(s, t):
    s=t[:]
    tasodifiy=random.choice(s)
    t+= tasodifiy
    
    return tasodifiy

s = ""
t = "y"

words=func(s, t)
print(words)