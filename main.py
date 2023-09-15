

class Stack:
    def __init__(self):
        self.stack = []


    def is_empty(self):
        if self.stack == []:
            return True
        return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return 'Стек пустой'
        remove_item = self.stack.pop()
        return remove_item

    def peek(self):
        if len(self.stack) == 0:
            return 'Стек пустой'
        return self.stack[-1]

    def size(self):
        return len(self.stack)

def is_balanced(string: str) -> str:
    s = Stack()
    list_string = list(string)
    not_balanced = 'Несбалансированно'
    for item in list_string:
        if item in ['(', '{', '[']:
            s.push(item)
        else:
            if s.is_empty():
                return not_balanced
            current_item = s.pop()
            if current_item == '(':
                if item != ')':
                    return not_balanced
            if current_item == '{':
                if item != '}':
                    return not_balanced
            if current_item == '[':
                if item != ']':
                    return not_balanced

    if s.is_empty():
        return 'Сбалансированно'
    return not_balanced

if __name__ == '__main__':

    print(is_balanced('(((([{}]))))'))
    print(is_balanced('[([])((([[[]]])))]{()}'))
    print(is_balanced('{{[()]}}'))
    print(is_balanced('}{}'))
    print(is_balanced('{{[(])]}}'))
    print(is_balanced('[[{())}]'))