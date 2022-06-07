class Node:
    def __init__(self, data):
        self.data= data
        self.next= None
        self.prev= None

class dll:
    def __init__(self):
        self.head= None
        self.tail= None

    def insertEnd(self, data):
        newNode= Node(data)
        if self.head is None:
            self.head= newNode
            self.tail= newNode
            return
        self.tail.next= newNode
        newNode.prev= self.tail
        self.tail= newNode


    def lenOfDll(self):
        count=0
        temp= self.head
        while temp is not None:
            count+=1
            temp= temp.next
        return count

    def deleteBeg(self):
        if self.head is None:
            print("Empty list...")
            return
        temp= self.head.next
        if temp is None:
            self.head= None
            return
        self.head.next= None
        temp.prev=None
        self.head= temp

    def deleteEnd(self):
        if self.head is None:
            print("Empty list...")
            return
        temp= self.tail.prev
        self.tail.prev= None
        temp.next= None
        self.tail= temp

    def deleteAtGivenPosn(self, i):
        n= self.lenOfDll()
        if i==0:
            return self.deleteBeg()
        if i==n:
            return self.deleteEnd()
        if i>n:
            print("Invalid Position...")
            return
        count=0
        temp= self.head
        while temp.next is not None and count is not (i-1):
            count+=1
            temp= temp.next
        temp1= temp.prev
        temp2= temp.next
        temp.prev= None
        temp.next= None
        temp1.next= temp2
        temp2.prev= temp1

    def printDll(self):
        temp= self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp= temp.next
        print()

def main():
    d= dll()
    n= int(input())
    arr= list(map(int, input().split()))
    for i in range(n):
        d.insertEnd(arr[i])
    d.printDll()
    d.deleteEnd()
    d.printDll()
    d.deleteAtGivenPosn(3)
    d.printDll()
    print(d.lenOfDll())


if __name__ == '__main__':
    main()
