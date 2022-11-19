# 스택: LIFO(후입선출), push, pop 연산 지원, ex. 쌓인 접시
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item

# 큐: 시퀀스의 한쪽 끝에는 엔티티를 추가하고 다른 반대쪽 끝에는 제거할 수 있는 엔티티 컬렉션이다. ex. 맛집 줄