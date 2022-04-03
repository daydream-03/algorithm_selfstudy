class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None

    def __str__(self):
        return str(self.key)


# 모든 노드를 변수로 담는 방법
a = Node(3)
b = Node(9)
c = Node(-1)
a.next = b
b.next = c

# 한방향 연결리스트 객체 = 헤드 노드만 이용하는 방법
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.head)

    def pushFront(self, key):
        new_node = Node(key)  # 노드 생성
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pushBack(self, key):
        new_node = Node(key)
        if len(self) == 0:  # 길이가 0인 연결리스트면 push back한 노드가 헤드 노드가됨
            self.head = new_node
        else:
            tail = self.head  # 연결리스트라 헤드부터 끝까지 훑어서 맨 마지막 노드를 찾는 수밖에 없음
            while tail.next != None:
                tail = tail.next
            tail.next = new_node
            self.size += 1

    def popFront(self):
        if len(self) == 0:
            return None
        else:  # 하나 이상의 노드가 존재
            x = self.head
            key = x.key
            self.head = x.next  # 헤드노드를 pop 하면 그 다음 노드가 헤드노드
            self.size -= 1
            del x
            return key

    def popBack(self):
        if len(self) == 0:
            return None
        else:
            prev, tail = None, self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            if len(self) == 1:
                self.head = None
            else:
                prev.next = tail.next
            key = tail.key
            del tail
            self.size -= 1
            return key

    def search(self, key):
        v = self.head
        while v != None:
            if v.key == key:
                return v
            v = v.next
        return None

    # for 반복문을 사용 가능케 하는 제너레이터
    def __iter__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next


my_sll = SinglyLinkedList()
my_sll.pushFront(-1)
my_sll.pushFront(9)
my_sll.pushBack(15)
my_sll.popFront()
my_sll.popBack()

print(my_sll.head.next)
print(len(my_sll))
print(my_sll)
print(my_sll.search(15))

for v in my_sll:  # __iter__
    print(v)
