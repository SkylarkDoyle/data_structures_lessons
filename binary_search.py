#binary search!!!

#target = 11

#arr = [1,3,4,5,8,4,0,11,8,9,3]
#Note----    O(1) + O(1) = O(1),          O(1) + O(n) = O(n),      O(1) + O(n^2) = O(n^2)


#Time Complexity -> O(1) + O(1) + n * O(1) | bcs of the  while loop |  + O(1) + O(1) + O(1) + O(1) = O(n) 
def search(arr, target):
    left_arr_index = 0                           #T= O(1)
    right_arr_index = len(arr) - 1   #T= O(1)
    while left_arr_index <= right_arr_index:
        mid = int((left_arr_index + right_arr_index) / 2) #T= O(1)
        if arr[mid] == target:
            return arr[mid] #T= O(1)
        elif target < arr[mid]:
            right_arr_index = mid - 1 #T= O(1)
        else:
            left_arr_index = mid + 1   #T= O(1)
    return -1 #no target then....  #T= O(1)
