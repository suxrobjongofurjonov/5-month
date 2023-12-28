def num(my_l):
    count={}
    for var in my_l:
        if isinstance(var, int) and 0<=var<=9:
            count[var] = count.get(var, 0) + 1
    for digit, count in count.items():
        if count == 1:
            return digit
    return None
print(num([1, 2, 3, 4, 5, 2, 3, 4, 1]))