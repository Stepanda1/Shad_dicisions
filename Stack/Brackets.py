s = '(({}[]))()'

def Brackets(s):
    stack = []
    brackets = {')':'(',']':'[','}':'{'}
    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or brackets[char] != stack.pop():
                return False
    return not stack

print(Brackets(s))