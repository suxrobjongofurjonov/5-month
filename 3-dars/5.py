def func(text, element):
    my_func=[]
    for var in text:
        my_func.append(var)
        
    res= [index for (index, item) in enumerate(my_func) if item == element]
    return res
       
print(func("Suxrob","m"))  