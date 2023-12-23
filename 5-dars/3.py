def buble_sort(my_l):
        res= len(my_l)-1
        sorted = False

        while not sorted:
            sorted = True 
            
            for i in range(0, res):
                if my_l[i]<my_l[i+1]:
                    sorted = False
                    my_l[i],my_l[i+1] = my_l[i+1], my_l[i]
                    
        return my_l


print(buble_sort([3,5,6,7,2,1]))