class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        x = self.head
        while x:
            nodes.append(repr(x))
            x = x.next
        return '[' + '-->'.join(nodes) + ']'

    def prepend(self, data):
        self.head = ListNode(data=data, next=self.head)

    def append(self, data):
        if not self.head:
            self.head = ListNode(data=data)
            return
        x = self.head
        while x.next:
            x = x.next
        x.next = ListNode(data=data)

    def find(self,index):
        x = self.head
        while x:
            if x.data[2] == index:
                break
            x = x.next
        return x

    def remove(self, index):
        x = self.head
        y = None
        while x and x.data[2] != index:
            y = x
            x = x.next
        # Unlink it from the list
        if y is None:
            self.head = x.next
        elif x:
            y.next = x.next
            x.next = None

n = LinkedList()
n.append(['DR.PIRA',35,1])
n.append(['ZEYNI',12,2])
n.append(['Shahin',21,3])


print(' SHOW THE ALL ITEMS ==>',n,'\n')
print('SEARCH THE 1 ID ==>',n.find(1),'\n')
n.remove(2)
print('REMOVE THE ID 2',n)



