
class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

class SLL:
    def __init__(self):
        self.head= None

    def lenOfSll(self):
        count=0
        temp= self.head
        while temp is not None:
            count+=1
            temp= temp.next
        return count

    """FIRST WE NEED TO INSERT THEN WE CAN DELETE"""
    def insertAtEnd(self, data):
        newNode= Node(data)
        if (self.head is None):
            self.head= newNode
        else:
            temp= self.head
            while (temp.next is not None):
                temp= temp.next
            temp.next= newNode

    """DELETE FROM END"""
    def deleteFromEnd(self):
        if (self.head is None):
            return
        if (self.head.next is None):
            self.head= None
        else:
            temp= self.head
            while (temp.next.next is not None):
                temp= temp.next
            self.tail= temp
            temp.next= None

    """DELETE FROM BEGINNING"""
    def deleteFromBeginning(self):
        if (self.head is None):
            return
        else:
            self.head= self.head.next

    """DELETE FROM THE GIVEN POSITION"""
    def delAtGivenPosn(self, i):
        n= self.lenOfSll()
        if i==0:
            return self.deleteFromBeginning()
        if i== n-1:

            return self.deleteFromEnd()
        if i>n-1:
            print("Invalid Position...")
            return
        count=0
        temp= self.head
        while temp.next is not None and count is not (i-1):
            count+=1
            temp= temp.next
        temp.next= temp.next.next

    """PRINT THE LINKED LIST"""
    def printSLL(self):
        temp= self.head
        while (temp is not None):
            print(temp.data, end=" ")
            temp= temp.next
        print()

def main():
    s= SLL()
    n= int(input())
    arr= list(map(int, input().split()))
    for i in range(n):
        s.insertAtEnd(arr[i])
    s.printSLL()
    s.delAtGivenPosn(0)
    s.printSLL()
    s.delAtGivenPosn(3)
    s.printSLL()

if __name__ == '__main__':
    main()
