def func(text1, text2):
    farq=[]
    for i in set(text1+text2):
        if text1.count(i) != text2.count(i):
            farq.append(i)
    return farq
s=""
t="y"

print(func(s,t))