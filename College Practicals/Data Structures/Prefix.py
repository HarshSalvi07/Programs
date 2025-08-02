#Stack ADT implementation
class Stack:
    def __init__ (self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
#Balanced Delimeter Checker with detailed comments
class DelimiterMatcher:
    def __init__(self):
        #Mapping of closing brackets to their corresponding opening brackets
        self.pairs = {')': '(', '}':'{',']':'['}

        def is_matching(self, code_string):
            #Create an empty stack to hold opening brackets
            stack = Stack()

            #Traverse each character in teh input string
            for char in code_string:

                if char in "([{" :
                    stack.push(char)

                #If the character is a closing bracket, match it
                elif char in ")]}":
                    #Step 1: If the stack is empty, there's no opening bracket
                    if stack.is_empty():
                        return False
                    
                    #Step 2: Pop the last opening bracket from the stack
                    top = stack.pop()

                    #Step 3: Get the expected matching opening bracket
                    expected_opening = self.pairs[char]

                    #Step 4: Compare the popped bracket with the expected one
                    if top != expected_opening:
                        return False #Mismatch found
                    
            #Step 5: After processing all characters, if the stack is empty, all brackets matched correctly
            return stack.is_empty()

class PrefixToPostfixConverter:
    def __init__(self):
        pass

    def is_operand(self,ch):
        return ch.isalpha() or ch.isdigit()
    
    def convert(self,prefix_expr):
        stack = Stack()
        for char in reversed(prefix_expr):
            if self.is_operand(char):
                stack.push(char)
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                new_expr = op1 + op2 + char
                stack.push(new_expr)
        return stack.pop()
    
#Test DelimiterMatcher

matcher = DelimiterMatcher()


