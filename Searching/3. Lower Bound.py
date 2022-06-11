def lowerBound(arr, n, ele):
    low= 0
    high= n
    while low< high:
        mid= (low+high)//2
        if arr[mid]>= ele:
            high= mid
        else:
            low= mid+1
    return low

from sys import setrecursionlimit
setrecursionlimit(100000000)

def main():
    t= int(input())
    while t>0:
        n= int(input())
        arr= list(map(int, input().split()))
        ele= int(input())
        print(lowerBound(arr, n, ele))
        t-=1

if __name__ == '__main__':
    main()
