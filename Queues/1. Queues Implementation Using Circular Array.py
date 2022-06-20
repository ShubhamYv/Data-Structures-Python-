class QueueUsingCircularArray:
    def __init__(self, capacity):
        self.que= [None]*capacity
        self.front= -1
        self.rear= -1
        self.size= 0
        self.cap= capacity

    """Is Empty Queue"""
    def isEmpty(self):
        return self.front==-1


    """Enqueue Operation"""
    def enqueue(self, data):
        #queue full or not...
        if (self.rear+1)%self.cap== self.front:
            print("Queue is Full...")
            return
        #queue is empty or not
        if self.isEmpty():
            self.front= self.rear=0
            self.que[self.rear]= data
            self.size+=1
            return
        self.rear= (self.rear+1)% self.cap
        self.que[self.rear]= data
        self.size+=1

    """Dequeue Operation"""
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty...")
            return
        #one ele in the queue.
        if self.rear== self.front:
            temp= self.que[self.front]
            self.front= self.rear= -1
            return temp
        temp= self.que[self.front]
        self.front= (self.front+1)%self.cap
        self.size-=1
        return temp

    """Front Element of Queue"""
    def frontEle(self):
        if self.isEmpty():
            print("Queue is Empty...")
            return
        return self.que[self.front]

    """Print the Queue"""
    def printQueue(self):
        if self.isEmpty():
            print("Queue is Empty...")
            return
        for i in range(self.size):
            print(self.que[(self.front+i)% self.cap], end=" ")
        print()

def main():
    cap= int(input())
    que= QueueUsingCircularArray(cap)
    for ele in input().split():
        que.enqueue(int(ele))
    que.printQueue()
    que.dequeue()
    que.printQueue()
    que.enqueue(1000)
    que.enqueue(150)
    que.printQueue()

if __name__ == '__main__':
    main()
