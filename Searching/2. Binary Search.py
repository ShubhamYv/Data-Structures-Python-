"""ITERATIVE"""

def binarySearch(arr, x):
    n= len(arr)
    low= 0
    high= n-1
    while low<= high:
        mid= low+ (high-low)//2
        if arr[mid]== x:
            return mid
        elif arr[mid]> x:
            high= mid-1
        else:
            low= mid+1
    return -1  # ele not present in array.
        
    
    
"""RECURSIVE"""    
    
# def binarySearch(arr,low, high, x):
#     while low> high:
#         return -1
#     mid= low+ (high-low)//2
#     if arr[mid]== x:
#         return mid
#     elif arr[mid]> x:
#         return binarySearch(arr, low, mid-1, x)
#     else:
#         return binarySearch(arr, mid+1, high, x)
    
    
def main():
    n= int(input())
    arr= list(map(int, input().split()))
    x= int(input())
    res= binarySearch(arr, x) #FOR ITERATIVE
#     res= binarySearch(arr, 0, n-1, x)  #For RECURSIVE
    
    if res== -1:
        print("Element not present...")
    else:
        print("Present at index: ", res)
if __name__ == '__main__':
    main()
