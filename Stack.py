class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        '''проверка стека на пустоту. Метод возвращает True или False.'''
        return True if self.size() == 0 else False

    def push(self, item: str):
        '''добавляет новый элемент на вершину стека. Метод ничего не возвращает'''
        self.stack.append(item)

    def pop(self):
        '''удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека'''
        self.stack.pop()

    def peek(self):
        '''возвращает верхний элемент стека, но не удаляет его. Стек не меняется.'''
        return self.stack[self.size()]

    def size(self):
        '''возвращает количество элементов в стеке'''
        return len(self.stack)
