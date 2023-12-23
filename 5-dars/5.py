def binary_search(my_list, value):
    start_l=0
    end_l=len(my_list)-1 
    count=0
    
    while start_l<=end_l:
        res=start_l+(end_l-start_l)//2
        res2=my_list[res]
        
        count=count+1
        if res==value:
            return (res, res2)
        
        elif value<res2:
            end_l=res-1
        
        else:
            start_l=res+1
            
    return None

print(binary_search([25,37,34,76,40,51], 40))