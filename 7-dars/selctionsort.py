### selection sort ###
# def selection_s(my_l):
#     index_length=range(0, len(my_l)-1)
    
#     for i in index_length:
#         min_v=i
        
#         for j in range(i+1, len(my_l)):
#             print(i,j)
#             if my_l[j]<my_l[min_v]:
#                 min_v=j
                
#         if min_v!=i:
#             my_l[min_v],my_l[i]=my_l[i],my_l[min_v]
            
#     return my_l
            
# print(selection_s([8,2,5,11,22,18]))

### quick sort ###
# def quick_sort(my_l):
#     length=len(my_l)
    
#     if length<=1:
#         return my_l
#     else:
#         pivot=my_l.pop()
#         print(pivot)
        
#     items_b=[]
#     items_s=[]
    
#     for i in my_l:
#         if i>pivot:
#             items_b.append(i)
#         else:
#             items_s.append(i)
            
#     return quick_sort(items_s)+[pivot]+quick_sort(items_b)
        
# print(quick_sort([17,15,2,4,25,6,7]))