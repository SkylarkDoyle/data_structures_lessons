#this is recursion for factorial
#Note----    O(1) + O(1) = O(1),          O(1) + O(n) = O(n),      O(1) + O(n^2) = O(n^2)



#Time Complexity -> O(n^2) + O(1) = O(n^2)  

def factorial(n):
    if n >= 1:
        return n * factorial(n - 1) #T= O(n^2)
    else:
        return 1 #T= O(1)

#Time Complexity -> O(n^2) + O(1) = O(n^2)  
def fib(n):
    if n >= 3:
        return fib(n-1) + fib(n-2) #T= O(n^2)
    else:
        return 1  #T= O(1)
    
