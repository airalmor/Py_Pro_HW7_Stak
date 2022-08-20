class Stack:
    def __init__(self, st=None):
        if st is None:
            st = []
        self.st = st

    def push(self, item):
        self.st.append(item)

    def pop(self):
        self.st.pop()
        return

    def peek(self):
        return self.st[-1]


def check_balance(quest: str):
    open_brackets = '({['
    close_brackets = ')}]'
    s = Stack()

    for i in quest:
        if i in open_brackets:
            s.push(open_brackets.index(i))
        elif i in close_brackets:
            if s.st and s.peek() == close_brackets.index(i):
                s.pop()
            else:
                print('Не сбалансирован')
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
