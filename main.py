from Stack import Stack


def isBalance(text: str):

    stack = Stack()

    for i in text:
        if i in ['{', '[', '(']:
            stack.push(i)
        elif i in ['}', ']', ')']:
            if stack.isEmpty():
                return False
            last_stack = stack.pop()

            if not ((last_stack == '(' and i == ')')
                    or not (last_stack == '[' and i == ']')
                    or not (last_stack == '{' and i == '}')):
                return False

    return stack.isEmpty()

if __name__ == '__main__':

    symbolString = input('Введите строку скобок: ')
    print(('Несбалансированно', 'Сбалансированно')[isBalance(symbolString)])

