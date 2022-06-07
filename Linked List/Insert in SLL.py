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

    """INSERT AT END WILL PRINT SAME ARRAY"""
    def insertAtEnd(self, data):
        newNode= Node(data)
        if (self.head is None):
            self.head= newNode
        else:
            temp= self.head
            while (temp.next is not None):
                temp= temp.next
            temp.next= newNode

    """INSERT AT END USING TAIL WILL PRINT SAME ARRAY"""
    # def insertAtEndTail(self, data):
    #     newNode= Node(data)
    #     if (self.head is None):
    #         self.head= newNode
    #         self.tail= newNode
    #     else:
    #         self.tail.next= newNode
    #         self.tail= newNode

    """INSERT AT BEGINNING WILL REVERSE THE ARRAY"""
    def insertAtBeginning(self, data):
        newNode= Node(data)
        if (self.head is None):
            self.head= newNode
        else:
            newNode.next=self.head
            self.head= newNode

    """INSERT AT THE i'th POSITION"""
    def insertAtithPosn(self, i, data):
        newNode= Node(data)
        n= self.lenOfSll()
        if (i==0):
            self.insertAtBeginning(data)
            return
        if i==n:
            self.insertAtEnd(data)
            return
        if i> n:
            print("Invalid Position...")
            return

        count= 0
        temp= self.head
        while (temp.next is not None and count is not (i-1)):
            count+=1
            temp= temp.next
        newNode.next= temp.next
        temp.next= newNode

    def printSLL(self):
        temp= self.head
        while (temp is not None):
            print(temp.data, end=" ")
            temp= temp.next
        print()

def main():
    s= SLL()
    s2= SLL()
    n= int(input())
    arr= list(map(int, input().split()))
    for i in range(n):
        # s.insertAtEndTail(arr[i])
        s.insertAtEnd(arr[i])
        s2.insertAtBeginning(arr[i])
    s.printSLL()
    s2.printSLL()
    s.insertAtithPosn(4,100)
    s.printSLL()

if __name__ == '__main__':
    main()
