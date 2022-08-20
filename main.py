class Stack:
    def __init__(self, st=None):
        if st is None:
            st = []
        self.st = st

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def push(self, item):
        self.st.append(item)

    def pop(self):
        self.st.pop()
        return

    def peek(self):
        return self.st[-1]

    def size(self):
        return len(self.st)


def check_balance(quest: str):
    open_brackets = '({['

    s = Stack()

    for i in quest:

        if i in open_brackets:
            s.push(i)
        else:
            if not s.isEmpty():
                if i == ')' and s.peek() == '(' \
                        or i == ']' and s.peek() == '[' \
                        or i == '}' and s.peek() == '{':
                    s.pop()
                else:
                    print('Не сбалансирован')
                    return
            else:
                print('Не сбалансированы')
                return
    if not s.isEmpty():
        print('Не сбалансированы')
        return

    return (print('Сбалансированы'))


if __name__ == '__main__':
    s = Stack()
    check_balance('(((([{}]))))')
    check_balance('[([])((([[[]]])))]{()}')
    check_balance('{{[()]}}')
    check_balance('}{}')
    check_balance('{{[(])]}}')
    check_balance('[[{())}]')
    check_balance(str(input('Введите свою строку')))
