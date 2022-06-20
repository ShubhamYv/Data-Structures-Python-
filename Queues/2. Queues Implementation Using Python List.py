class queueUsingList:
    def __init__(self):
        self.que= []
        self.size= 0
        self.front= 0

    """Enqueue operation"""
    def enqueue(self, data):
        self.que.append(data)
        self.size+=1

    """Is Empty Queue"""
    def isEmpty(self):
        return self.size==0

    """Dequeue Operation"""
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty...")
            return
        temp= self.que[self.front]
        self.front+=1
        self.size-=1
        return temp

    """Front ele of Queue"""
    def frontEle(self):
        if self.isEmpty():
            print("Queue is Empty...")
            return
        return self.que[self.front]

    """Print Queue"""
    def printQueue(self):
        if self.isEmpty():
            print("Queue is Empty...")
            return
        for i in range(self.size):
            print(self.que[self.front+i], end=" ")
        print()

def main():
    cap= int(input())
    que= queueUsingList()
    for ele in input().split():
        que.enqueue(ele)
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
    
    
    
    
"""
INPUT: 
10
2 3 1 4 5 6 4 3 5 4
OUTPUT:
2 3 1 4 5 6 4 3 5 4 
2
3
1
5 6 4 3 5 4 
6 4 3 5 4 10000 
6 4 3 5 4 10000 140 
"""
