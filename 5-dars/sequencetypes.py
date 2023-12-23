### SEQUENCE TYPES
# sequence_types=[1,2,3,4,5]
# print(sequence_types.index(5))
# sequence_types=[1,2,3,4,5]
# sequence_types[2]=15
# print(sequence_types)
### str va tuple immutable = ozqarmas, list mutable = ozqaruvchan
# sequence='Suxrob'
# sequence[4]='a'
# print(sequence)
### binary search- bu kitobdagi sahifalarni qidirishga oxshatish mumkin, lekin tartibsz datalarda ishlamaydi ex:Dictionary
# def binary_search(my_list, value):
#     start_index=0
#     end_index=len(my_list)-1
#     count=0
#     while start_index<=end_index:
#         mid_point=start_index+(end_index-start_index)//2
#         mid_point_val=my_list[mid_point]
        
#         count=count+1
        
#         if mid_point_val==value:
#             return (mid_point, mid_point_val)
            
#         elif value<mid_point_val:
#             end_index=mid_point-1
        
#         else:
#             start_index=mid_point+1
            
    
#     return None
        
# print(binary_search([5,7,9,79,45,56], 45)) 
    
# def binary_search(my_list, value):
#     start_l=0
#     end_l=len(my_list)-1 
#     count=0
    
#     while start_l<=end_l:
#         res=start_l+(end_l-start_l)//2
#         res2=my_list[res]
        
#         count=count+1
        
#         if res==value:
#             return (res, res2)
        
#         elif value<res2:
#             end_l=res-1
        
#         else:
#             start_l=res+1
            
#     return None

# print(binary_search([25,37,34,76,40,51], 40))

###  buble search ###
# def buble_sort(my_l):
#     len_index=len(my_l)-1
#     sorted=False
#     count=0
#     while not sorted:
#         sorted= True
        
#         for i in range(0, len_index):
#             count=count+1
#             if my_l[i]>my_l[i+1]:
#                 sorted=False
#                 my_l[i],my_l[i+1]=my_l[i+1],my_l[i]
                
#     return my_l,count

# print(buble_sort([10,2,4,12,8,11,3,5,6,76,9]))

# def bubble_s(arr):
#     n=len(arr)
#     count=0
#     for a in range(n-1):
#         swap=False
        
        
#         for a in range(0, n-1):
#             if arr[a]>arr[a+1]:
#                 arr[a],arr[a+1]=arr[a+1],arr[a]
#                 count=count+1
#                 swap=True
        
#         if not swap:
#             break
#     return arr,count
    
# arr=[1,2,5,2,7,6] 

# print(bubble_s(arr))

