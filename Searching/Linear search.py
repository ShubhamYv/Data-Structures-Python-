def linearSearch(arr, x):
    n= len(arr)
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

def main():
    n= int(input())
    arr= list(map(int, input().split()))
    x= int(input())
    print(linearSearch(arr, x))

if __name__ == '__main__':
    main()
