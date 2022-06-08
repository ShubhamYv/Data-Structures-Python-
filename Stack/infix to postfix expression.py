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


def precedence(str):
        if str== "^":
            return 3
        if str== "*" or str=="/":
            return 2
        if str=="+" or str=="-":
            return 1
        if str==")" or str=="(":
            return -1
        else:
            return 0

def main():
    st= Stack()
    arr= list(map(int, input().split()))
    ans=""
    for i in range(len(arr)):
        val= precedence(arr[i])
        if val==0:
            ans+= arr[i]
        else:
            if arr[i]== "(":
                st.push(arr[i])
            elif arr[i]== ")":
                while st.isEmpty() is False and st.tos()!= "(":
                    ans+= st.tos()
                    st.pop()
                if st.tos()== "(":
                    st.pop()

            else:
                while st.isEmpty() is False and precedence(arr[i]> precedence(st.tos())):
                    ans+= st.tos()
                    st.pop()
                st.push(arr[i])

    while st.isEmpty() is False:
        ans+= st.tos()
        st.pop()
    print(ans)

if __name__ == '__main__':
    main()
