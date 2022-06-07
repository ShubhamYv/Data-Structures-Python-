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

    def insertBeg(self, data):
        newNode= Node(data)
        if self.head is None:
            self.head= newNode
            self.tail= newNode
            self.tail.next= self.head
            return
        newNode.next= self.head
        self.head= newNode
        self.tail.next= self.head

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

    def insertAtGivenPosition(self, i, data):
        newNode= Node(data)
        n= self.lenOfCll()
        if i==0:
            return self.insertBeg(data)
        if i==n:
            return self.insertEnd(data)
        if i>n:
            print("Invalid position...")
            return
        count=0
        temp= self.head
        while temp.next is not None and count is not (i-1):
            count+=1
            temp= temp.next
        newNode.next= temp.next
        temp.next= newNode


    def printCll(self):
        temp= self.head
        while True:
            print(temp.data, end=" ")
            temp= temp.next
            if temp== self.head:
                break
        print()

def main():
    c= cll()
    c1= cll()
    arr= list(map(int, input().split()))
    for i in range(len(arr)):
        c.insertBeg(arr[i])
        c1.insertEnd(arr[i])
    c.printCll()
    c1.printCll()
    c1.insertAtGivenPosition(0, 1000)
    c1.printCll()
    print(c.lenOfCll())

if __name__ == '__main__':
    main()
