class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

class cll:
    def __init__(self):
        self.head= None
        self.tail= None

    def lenOfCll(self):
        count=1
        temp= self.head
        while temp is not self.tail:
            count+=1
            temp= temp.next
        return count

    def insertEnd(self, data):
        newNode= Node(data)
        if self.head is None:
            self.head= newNode
            self.tail= newNode
            self.tail.next= self.head
            return
        self.tail.next= newNode
        self.tail= newNode
        self.tail.next= self.head

    def deleteBeg(self):
        if self.head is None:
            print("Empty list...")
            return
        if self.head.next is self.head:
            self.head= None
            self.tail= None
            return
        self.head= self.head.next
        self.tail.next= self.head


    def deleteEnd(self):
        if self.head is None:
            print("Empty list...")
            return
        if self.head.next is self.head:
            self.head= None
            self.tail= None
            return
        temp= self.head
        while temp.next is not self.tail:
            temp= temp.next
        self.tail.next= None
        self.tail= temp
        self.tail.next= self.head

    def delAtithPosn(self, i):
        n= self.lenOfCll()
        if i==0:
            return self.deleteBeg()
        if i== n:
            return self.deleteEnd()
        if i>n:
            print("Invalid Position...")
            return
        count=0
        temp= self.head
        while temp.next is not None and count is not (i-1):
            count+=1
            temp= temp.next
        temp.next = temp.next.next

    def printCll(self):
        count= 1
        temp= self.head
        while True:
            print(temp.data, end=" ")
            temp= temp.next
            if temp== self.head:
                break
        print()

def main():
    c= cll()
    n= int(input())
    arr= list(map(int, input().split()))
    for i in range(n):
        c.insertEnd(arr[i])
    c.printCll()
    c.deleteEnd()
    c.printCll()
    c.delAtithPosn(2)
    c.printCll()

if __name__ == '__main__':
    main()
