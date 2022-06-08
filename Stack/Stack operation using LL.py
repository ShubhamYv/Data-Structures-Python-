class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

class Stack:
    def __init__(self):
        self.head= None
        self.top=-1

    """TO CHECK WHETHER THE STACK IS EMPTY OR NOT"""
    def isEmpty(self):
        if (self.head is None):
            return True
        return False

    """PUSH OPERATION USING INSERT AT THE BEGINNING"""
    def push(self,data):
        newNode= Node(data)
        if (self.head is None):
            self.head= newNode
            self.top+=1
            return
        newNode.next= self.head
        self.head= newNode
        self.top+=1

    """POP OPERATION USING DELETE FROM THE BEGINNING"""
    def pop(self):
        if (self.isEmpty()):
            print("Stack is empty")
            return
        self.head= self.head.next
        self.top-=1

    """TO CHECK THE SIZE OF STACK"""
    def size(self):
        return self.top+1

    """TO KNOW THE VALUE OF TOP ELEMENT"""
    def tos(self):
        if (self.isEmpty()):
            print("Stack is empty")
            return
        return self.head.data

def main():
    st= Stack()
    n= int(input())
    for ele in input().split():
        st.push(int(ele))
    print(st.size())
    while (st.size() != 0):
        print(st.tos())
        st.pop()

if __name__ == '__main__':
    main()

