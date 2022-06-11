def upperBound(arr, n, ele):
    low= 0
    high= n
    while low< high:
        mid= (low+high)//2
        if ele >= arr[mid]:
            low = mid + 1
        else:
            high= mid
    return low

from sys import setrecursionlimit
setrecursionlimit(100000000)

def main():
    t= int(input())
    while t>0:
        n= int(input())
        arr= list(map(int, input().split()))
        ele= int(input())
        print(upperBound(arr, n, ele))
        t-=1

if __name__ == '__main__':
    main()
