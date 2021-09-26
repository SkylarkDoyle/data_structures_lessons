#main function    Note----    O(1) + O(1) = O(1),          O(1) + O(n) = O(n),      O(1) + O(n^2) = O(n^2)

def quicksort(arr):
    qs(arr, 0, len(arr) - 1) # r -> index 0 and l -> amount of element in arr,    Time Complexity -> O(1)


#Time Complexity -> O(1) + O(1) +  O(n^2) + O(n^2) = O(n^2)  
def qs(arr, l, r):
    if l >= r:
        return # if l arrow >= r arrow just return the whole function(error), T= O(1)
    else:
        #else create assign a function to a variable P
        p = partition(arr, l, r) #T= O(1)
        qs(arr, l, p -1) #recursive function that arrange the right side of the partitions   T=O(n^2)
        qs(arr, p + 1, r) #recursive function that arrange the left side of the partitions   T=O(n^2)



#Time Complexity -> O(1) + O(1) + n * O(1)| bcs of the for loop |+ O(1) + O(1) + O(1) + O(1) = O(n) 
#function that creates the partition
def partition(arr, l, r):
    pivot = arr[r] #pivot -> the value of the last index                T= O(1)
    i = l - 1 #I variable will be outside  the function at first         T= O(1)
    
#let j be inside the function -> from the first array index to the second last index
    for j in range(l, r): 
        #if the value of j index < pivot 
        if arr[j] < pivot:
            #increment i variable by 1
            i += 1   #T= O(1)
            #swap the value index of i and j if J < pivot
            arr[i], arr[j] = arr[j], arr[i]                 #T= O(1)
    #swap the pivot with the middle index after the loop swaps
    arr[i + 1], arr[r] = arr[r], arr[i + 1]         #T= O(1)
    return i + 1                                                           #T= O(1)


#end of quicksort (sort) :)            
    


    
