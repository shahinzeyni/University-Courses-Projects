import sys

class Stack:
    lst = []
    top = -1

    def __init__(self,data):
        self.data = data

    '''Push item in the stack'''

    def Push(self, item):
        if self.top >= self.data - 1:
            print("Stack is full")

        else:
            self.lst.insert(self.top + 1,item)
            self.top = self.top + 1
            print(self.lst)

    '''delete the last item in Stack'''

    def Pop(self):
        print(self.top)
        if self.top == -1:
            print("stack is empty")
        else:
            d = self.lst[self.top]
            self.lst.pop(self.top)
            self.top = self.top - 1
            print(self.lst)
            print(d)

    '''check stack is empty'''

    def empty(self):
        if self.top == -1:
            return 'is Empty'
        else:
            return '\nThere is some Value'


p = int(input('Enter size of stack:'))
print('Items of Stack is-->',p ,'\n')
x = Stack(p)
i = 0
while 0< p:
    c = input('Enter:')
    x.Push(c)
    i+=1
    if i==p:
        break

x.Pop()
x.Pop()

print(x.empty())

sys.exit('End the program')

