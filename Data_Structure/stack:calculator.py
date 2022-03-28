class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, val):
        self.stack_list.append(val)

    def pop(self):
        try:
            return self.stack_list.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.stack_list[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.stack_list)


stack = Stack()
postfix = []


def prefer(x):
    if x == "*" or "/":
        return 2
    elif x == "+" or "-":
        return 1
    elif x == "(" or ")":
        return 0


# 6+(3-2)*4
# 6 3 2 - 4 * +
infix = "6+(3-2)*4"

for i in infix:
    if i.isdigit():
        postfix.append(i)
    elif i == "(":
        stack.push(i)
    elif i == ")":
        while len(stack) > 0:
            j = stack.pop()
            if j == "(":
                break
            postfix.append(j)
    elif i in "()+-*/":
        while prefer(i) < prefer(stack.top()):
            postfix.append(stack.pop())
        else:
            stack.push(i)

while len(stack) > 0:
    postfix.append(stack.pop())

print("stack : ", stack.stack_list)
print("postfix : ", postfix)
