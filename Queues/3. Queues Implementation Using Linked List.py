class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

class queueUsingLinkedList:
    def __init__(self):
        self.head= None
        self.tail= None
        self.size= 0

    """Is Empty"""
    def isEmpty(self):
        return self.size==0

    """Enqueue Operation"""
    def enqueue(self, data):
        newNode= Node(data)
        if self.head is None:
            self.head= self.tail= newNode
            self.size+=1
            return
        self.tail.next= newNode
        self.tail= newNode
        self.size+=1

    """Dequeue Operation"""
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty...")
            return
        if self.size==1:
            temp= self.head.data
            self.head= self.tail= None
            self.size-=1
            return temp
        temp= self.head.data
        self.head= self.head.next
        self.size-=1
        return temp

    """Front Element"""
    def frontEle(self):
        if self.isEmpty():
            print("Queue is Empty...")
            return
        return self.head.data

    """Print Queue Elements"""
    def printQueue(self):
        if self.isEmpty():
            print("Queue is Empty...")
            return
        temp= self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp= temp.next
        print()

def main():
    cap= int(input())
    que= queueUsingLinkedList()
    for ele in input().split():
        que.enqueue(int(ele))
    que.printQueue()
    n=3
    while n>0:
        print(que.frontEle())
        que.dequeue()
        n-=1
    que.dequeue()
    que.printQueue()
    que.dequeue()
    que.enqueue(10000)
    que.printQueue()
    que.enqueue(140)
    que.printQueue()

if __name__ == '__main__':
    main()
    
    
""""
INPUT:
10
2 3 1 4 5 6 7 5 8 0
OUTPUT:
2 3 1 4 5 6 7 5 8 0 
2
3
1
5 6 7 5 8 0 
6 7 5 8 0 10000 
6 7 5 8 0 10000 140 
"""
