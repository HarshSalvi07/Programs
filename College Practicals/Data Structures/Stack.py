class Stack:
    def __init__ (self):
        self.s = []

    def push(self, data):
        self.s.append(data)
        return

    def pop(self):
        self.s.pop(-1)
        return

    def isEmpty(self):
        return 0 == len(self.s)

    def peek(self):
        return self.s[-1]

    def show(self):
        print(self.s)
        return

def helper(a,b):
    if a == "(" and b == ")":
        return True
    elif a == "{" and b == "}":
        return True
    elif a == "[" and b == "]":
        return True
    else:
        return False

def delimeter(eqn):
    s = Stack()
    for i in eqn:
        if i in ["(","{","["]:
            s.push(i)
        elif i in [")","}","]"]:
            if not s.isEmpty() and helper(s.peek(), i):
                s.pop()
            else:
                return False
    return s.isEmpty()
      


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.peek()
    s.show()
    
    eqn = "(a+b(a-b))"
    eqn1 = "(s+b[g+h)"
    eqn2 = "(a+b(a-b}))"

    print(eqn,delimeter(eqn))
    print(eqn1,delimeter(eqn1))
    print(eqn2,delimeter(eqn2))
            
                  
        
    
        
