
def found(text):
    unlihar="aeiouAEIOU"
    my_list=list(text)
    var,i=0, len(my_list)-1

    while var<i:
        while var<i and my_list[var] not in unlihar:
            var+= 1
        while var<i and my_list[i] not in unlihar:
            i-= 1
        my_list[var], my_list[i] = my_list[i], my_list[var]
        var+=1
        i-=1

    return ''.join(my_list)

matn="Leetcode"
res=found(matn)
print(res)