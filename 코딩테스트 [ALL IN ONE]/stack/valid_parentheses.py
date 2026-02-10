# 잘못된 풀이법
## 반례: ")(){}" 이외에도 무수히 많음

def vaild_parenttheses(s):
    stack = []
    if len(s) <= 1:
        return False
    
    for c in s:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        if stack:
            char = stack[-1]
            if c == ')':
                if char == '(':
                    stack.pop()
                else:
                    return False
            if c == '}':
                if char == '{':
                    stack.pop()
                else:
                    return False
            if c == ']':
                if char == '[':
                    stack.pop()
                else:
                    return False
                
    return True if len(stack) == 0 else False
            

# print(vaild_parenttheses(")("))
# print(vaild_parenttheses("([]}"))
# print(vaild_parenttheses("{()[]}"))
# print(vaild_parenttheses("(([{})])"))
# print(vaild_parenttheses("[[{}]]()"))
# print(vaild_parenttheses("(({[]}()[[]]))"))
# print(vaild_parenttheses("]"))
print(vaild_parenttheses(")"))
