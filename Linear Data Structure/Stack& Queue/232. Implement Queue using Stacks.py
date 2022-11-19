# 풀이1. 스택 2개 사용
class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []   # 큐로 스택을 만들 때는 뒤로 넣고 앞으로 뺄 수 있어서 구현이 가능했지만 스택은 뒤로 넣고 뒤로 빼야하므로
                           # 앞선 문제처럼 구현할 수 없으므로 두개의 스택을 이용해 역순으로 담아야 한다.
    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:  # 큐에서 처음 있는 요소를 조회
        # output 없으면 모두 재입력
        if not self.output: # 없으면 최근에 추가한 요소가 앞으로 들어가게 됨
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output == []
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()