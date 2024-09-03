import sys
class Q:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def isempty(self):
        if self.items == []:
            return 'empty'

    def print_all(self):
        c = self.items
        while c:
            if self.items == []:
                return 'empty'
            else:
                print(c,'is my list \n')
            break

p = Q()
p.enqueue(1)
p.enqueue(2)
p.enqueue(3)

p.print_all()
print(f'`{p.dequeue()}` is dequeue')

p.print_all()
print(f'`{p.dequeue()}` is dequeue')

p.print_all()
print(f'`{p.dequeue()}` is dequeue')

p.print_all()
p.print_all()

print(p.isempty())

'''print and show the end text notif'''

sys.exit('End the Program')


