class Stack:
    def __init__(self):
        self.arr=[]
        self.top=-1

    def isEmpty(self):
        return self.top==-1

    def push(self, data):
        self.top+=1
        self.arr.append(data)

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        self.top-=1
        self.arr.pop()

    def size(self):
        return self.top+1

    def tos(self):
        if (self.isEmpty()):
            print("Stack is empty")
            return
        return self.arr[self.top]

def main():
    st= Stack()
    n= int(input())
    for ele in input().split():
        st.push(int(ele))
    print(st.size())
    while (st.size()!=0):
        print(st.tos())
        st.pop()

if __name__ == '__main__':
    main()

"""
i/p: 5
     1 2 3 4 5
o/p:     
     size --> 5
     stack--> 5
              4
              3
              2
              1
"""
