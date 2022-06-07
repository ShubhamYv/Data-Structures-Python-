class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertBeg(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

    def insertEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return

        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

    def printDLL(self):
        temp = self.head
        while temp is not None:
            # print(temp.prev, end=" ")
            print(temp.data, end=" ")
            temp = temp.next
        print()


def main():
    l = DLL()
    l1= DLL()
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        l.insertBeg(arr[i])
        l1.insertEnd(arr[i])
    l.printDLL()
    l1.printDLL()


if __name__ == "__main__":
    main()
