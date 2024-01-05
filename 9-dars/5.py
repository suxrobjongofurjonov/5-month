from collections import Counter
def func(ьн_list):
       
    words=''.join(ьн_list)
       
    l_count=Counter(words)
    
    letters=[letter for letter, count in l_count.items() if count > 1]
    
    return letters

print(func(["bella", "label", "roller"]))